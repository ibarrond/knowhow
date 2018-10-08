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
