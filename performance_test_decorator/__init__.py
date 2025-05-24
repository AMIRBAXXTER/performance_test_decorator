import time
import sys
import io
from functools import wraps


def performance_test(test_count=1000, show_result=True):
    """
    A decorator to measure the execution time of a function and optionally display the result of the first call.

    Args:
        test_count (int): The number of times the function is executed in the test. Defaults to 1000.
        show_result (bool): Whether to print the result of the first call to the decorated function. Defaults to True.

    Returns:
        A decorator function that takes a function as its argument and returns a function that takes the same arguments as the original function and returns the same result as the original function.

    The decorator works by capturing the output of the decorated function, executing it the specified number of times, and then restoring the original stdout. The result of the first call is optionally printed.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Testing {func.__name__}...\nplease wait...')
            saved_stdout = sys.stdout
            sys.stdout = io.StringIO()
            try:
                start = time.time()
                result = None
                for i in range(test_count):
                    temp = func(*args, **kwargs)
                    if i == 0:
                        result = temp
                end = time.time()
            finally:
                sys.stdout = saved_stdout

            print(f'{func.__name__} took {end - start:.4f} seconds to execute {test_count} times')
            if show_result:
                print(f'Result: {result if result is not None else "no result returned"}')
            return result

        return wrapper

    return decorator
