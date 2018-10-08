Timing your functions is necessary in all Machine Learning, to understand where to optimize when things are running slow, or to have a first idea on how long would an algorithm take to run if you used a huge dataset instead of a small portion of it. 

There are multiple ways to measure timing functions in Python. You can measure the initial time with `time.time()`, do it angain after the function and substract to obtain the elapsed time. More accurate clocks such as `time.perf_counter()` (to have an accurate time lapse) or `time.process_time()` (to have an accure=ate time lapse without waiting periods) are recommended in this case. However, this requires you to perform a very repetitive action: store time before, store time after, substract both. These 3 lines of code would be repeated everywhere in a piece of code you want to time. To avoid it, and to keep a beautiful codin style, we can use a **Timing Decorator**, basically a Python _Decorator_ created by me using seceral code snippets ([This one](https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python)).

The code would be the following (for convenience, this code is also included in a file named `Timing.py`):

        from typing import Dict
        from functools import wraps
        from time import process_time

        # PythonDecorators/decorator_with_arguments.py
        class Timing(object):
            """Timing Decorator Class

            A decorator for time measuring of functions.

            Example:
              # Create a timing dictionary: keys are strings, values are floats
              timing_dict: Dict[str, float] = {}

              # Apply the decorator and run the function
              @Timing(timing_dict, 'ny_fun1000')
              def my_fun(1000)
            """

            def __init__(self,
                         timings_dict: Dict[str, float]={},
                         timing_name: str='',
                         flag_print:  bool=True):
                self.timings_dict = timings_dict
                self.timing_name = timing_name
                self.flag_print = flag_print


            def __call__(self, f):
                """

                """
                @wraps(f)
                def wrapped_f(*args, **kw):
                    ts = process_time()  # Before
                    f(*args, **kw)       # Execute f
                    te = process_time()  # After

                    # Save time in timings_dict
                    if(not self.timing_name): self.timing_name = f.__name__
                    self.timings_dict[self.timing_name] = (te - ts)*1000

                    # Print timing
                    if(self.flag_print):
                      print('TIMING: %r -> %.6f ms\n' % (f.__name__,(te - ts)*1000))
                return wrapped_f
