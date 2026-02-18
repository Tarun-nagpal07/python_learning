'''Create a MethodLogger class with a @MethodLogger.log class method decorator that logs
the method name, arguments, and return value via the logging module each time it is called.'''


import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class MethodLogger:
    @classmethod
    def log(cls, func):
     
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_list = [repr(a) for a in args] + [f"{k}={v!r}" for k,v in kwargs.items()]
            logging.info(f"Calling: {func.__name__}({', '.join(arg_list)})")
            
            result = func(*args, **kwargs)
            
            logging.info(f"{func.__name__} returned: {result!r}")
            
            return result
        return wrapper


@MethodLogger.log
def add(a, b):
    return a + b

@MethodLogger.log
def multiply(a, b):
    return a * b

x = add(3, 4)
y = multiply(a=5, b=6)
