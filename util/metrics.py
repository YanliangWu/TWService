import time
from functools import wraps

def calculate_elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = round(time.time() - start_time, 3)
        print(f"Time elapsed for {func.__name__}: {elapsed_time} seconds")
        return result
    return wrapper