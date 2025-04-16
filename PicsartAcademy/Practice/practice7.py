# Sun 13 Apr 2025
from functools import wraps
import time
from typing import Callable


# Write a function my_decorator that wraps another function and prints "Function is called" before it runs.
def my_decorator(func):
    if not isinstance(func, Callable):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function is called")
        return func(*args, **kwargs)

    return wrapper


# Write a decorator log_args that prints the arguments and keyword arguments passed to a function.
def log_args(func):
    if not isinstance(func, Callable):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


# Make a decorator repeat(times) that repeats the function times.
def repeat(times):
    if not isinstance(times, int) or times < 1:
        raise ValueError("times must be a positive integer")

    def decorator(func):
        if not isinstance(func, Callable):
            raise TypeError("func must be callable")

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# Write a decorator @memoize that caches function results in a dictionary based on the input arguments.
def memoize(func):
    if not isinstance(func, Callable):
        raise TypeError("func must be callable")
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# Implement a decorator time_it that measures the time taken by a function to execute and prints it.
# Apply this decorator to a function that calculates the sum of squares of numbers from 1 to 1000.
def time_it(func):
    if not isinstance(func, Callable):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result

    return wrapper


# Implement a memoization decorator memoize that caches the results of a function to improve performance.
# Apply this decorator to a recursive function that computes the Fibonacci sequence.
# Demonstrate the speed improvement by calling the decorated function multiple times.
def memoize(func):
    if not isinstance(func, Callable):
        raise TypeError("func must be callable")
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    if not n or n < 1:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.time()
print(fibonacci(35))  # First call, should take longer
end_time = time.time()
print(f"First call took: {end_time - start_time} seconds")

start_time = time.time()
print(fibonacci(35))  # Second call, should be faster due to memoization
end_time = time.time()
print(f"Second call took: {end_time - start_time} seconds")