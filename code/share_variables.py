import functools

import tensorflow as tf


class share_variables(object):

  def __init__(self, callable_):
    self._callable = callable_
    self._wrappers = {}
    self._wrapper = None

  def __call__(self, *args, **kwargs):
    return self._function_wrapper(*args, **kwargs)

  def __get__(self, instance, owner):
    decorator = self._method_wrapper
    decorator = functools.partial(decorator, instance)
    decorator = functools.wraps(self._callable)(decorator)
    return decorator

  def _method_wrapper(self, instance, *args, **kwargs):
    if instance not in self._wrappers:
      name = self._create_name(
          type(instance).__module__,
          type(instance).__name__,
          instance.name if hasattr(instance, 'name') else id(instance),
          self._callable.__name__)
      self._wrappers[instance] = tf.make_template(
          name, self._callable, create_scope_now_=True)
    return self._wrappers[instance](instance, *args, **kwargs)

  def _function_wrapper(self, *args, **kwargs):
    if not self._wrapper:
      name = self._create_name(
          self._callable.__module__,
          self._callable.__name__)
      self._wrapper = tf.make_template(
          name, self._callable, create_scope_now_=True)
    return self._wrapper(*args, **kwargs)

  def _create_name(self, *words):
    words = [str(word) for word in words]
    words = [word.replace('_', '') for word in words]
    return '_'.join(words)
