import functools
import time


def ex_time(func):
    """writes execution time"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Execution time: {elapsed_time:.10f} seconds")
        return result

    return wrapper
