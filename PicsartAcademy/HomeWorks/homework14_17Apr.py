# 14 17 april 2025

from functools import wraps
from typing import Callable
import time


# Write a decorator repeat that repeats the execution of the decorated function n times, where n is provided as an argument to the decorator.
def repeat(n: int):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    def decorator(function: Callable):
        if not callable(function):
            raise TypeError(f"{type(function)} is not callable")

        @wraps(function)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(function(*args, **kwargs))
            return results

        return wrapper

    return decorator


#Implement a decorator memoize that caches the results of the decorated function to avoid redundant computations.
def memoize(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    cache = {}

    @wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return wrapper

#Create a decorator delay that delays the execution of the decorated function by n seconds, where n is provided as an argument.
def delay(n: int):
    if not isinstance(n, (int, float)) or n < 0:
        raise ValueError("n must be a non-negative number")

    def decorator(function: Callable):
        if not callable(function):
            raise TypeError(f"{type(function)} is not callable")

        @wraps(function)
        def wrapper(*args, **kwargs):
            time.sleep(n)
            return function(*args, **kwargs)

        return wrapper

    return decorator

#Create a decorator run_once that ensures a function can only be executed once. On subsequent calls, it should print a message indicating that the function has already been executed. Test it on a function that initializes a resource.
def runOnce(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    has_run = False

    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal has_run
        if has_run:
            print("This function has already been executed.")
            return
        has_run = True
        return function(*args, **kwargs)
    return wrapper

#Implement a decorator ensure_unique_call that prevents a function from being called with the same arguments more than once. If called with the same arguments, it should return the previous result.
def ensureUniqueCall(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    seen_args = set()

    @wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in seen_args:
            print("This function has already been called with these arguments.")
            return
        seen_args.add(key)
        return function(*args, **kwargs)

    return wrapper