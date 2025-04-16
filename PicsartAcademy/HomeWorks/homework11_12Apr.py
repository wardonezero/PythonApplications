# 11/12 April 2025

from functools import wraps
from typing import Callable
import time


# Write a decorator greet_decorator that adds a greeting message before and after the execution of the decorated function.
def greetDecorator(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Howdy!")
        result = function(*args, **kwargs)
        print("Goodbye!")
        return result

    return wrapper


# Create a decorator log_execution that logs the name of the function being executed along with its arguments and return value.


def logExecution(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(
            f"Executing {function.__name__} with arguments: {args} and keyword arguments: {kwargs}"
        )
        result = function(*args, **kwargs)
        print(f"{function.__name__} returned: {result}")
        return result

    return wrapper


# Write a decorator execution_timer that measures and prints the time taken by the decorated function to execute.
def executionTimer(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(
            f"{function.__name__} took {(end_time - start_time):.8f} seconds to execute"
        )
        return result

    return wrapper


# Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True. If not, raise an exception.
is_logged_in = False


def requireLogin(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    @wraps(function)
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            raise PermissionError("User is not logged in")
        return function(*args, **kwargs)

    return wrapper
