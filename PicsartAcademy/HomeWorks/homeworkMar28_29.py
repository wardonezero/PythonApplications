from collections.abc import Iterable
# Write a generator function called simple_sequence(start, end) that takes two integers (start and end) and yields each integer from start to end (inclusive).
def simpleSequence(start: int, end: int):
    if not isinstance(start, int) or not isinstance(end, int):
        yield 0
        return
    if start == end:
        return start
    if start > end:
        while start >= end:
            yield start
            start -= 1
    else:
        while start <= end:
            yield start
            start += 1


# Write a generator function countdown(n) that starts at n and counts down to 1, yielding each number.
def contdown(number: int):
    if not isinstance(number, int) or number < 1:
        yield 0
    else:
        while number > 0:
            yield number
            number -= 1


# Write a generator function fibonacci(limit=None) that yields Fibonacci numbers.
def fibonacci(limit=None):
    if not isinstance(limit, int) or limit < 0 and limit is not None:
        return -1
    else:
        first = 0
        second = 1
        while limit is None or first < limit:
            yield first
            first, second = second, first + second


# for i in fibonacci():
#     print(i)
#     if i > 100:
#         break


# Write a generator function even_numbers(nums) that takes a list (or any iterable) of integers and yields only those that are even.
def evenNumbers(numbers):
    if not isinstance(numbers, Iterable) and not all(
        isinstance(item, (int, float)) for item in numbers
    ):
        yield 0
    else:
        for number in numbers:
            if number % 2 == 0:
                yield number


print(list(evenNumbers([1, 2, 3, 4, 5, 6])))


# Write a generator function cumulative_sum(nums) that takes a list (or any iterable) of numbers.
def comulativeSum(numbers):
    if not isinstance(numbers, (list, tuple)) and not all(
        isinstance(item, (int, float)) for item in numbers
    ):
        yield 0
    else:
        total = 0
        for number in numbers:
            total += number
            yield total
