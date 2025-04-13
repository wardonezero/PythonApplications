# 31 March / 5 April

# Write a program to identify all prime numbers between 1 and 100 using list comprehensions.
primeList = [
    num
    for num in range(2, 101)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]
print(primeList)


ls = [1, 2, -3, 4, -5, -6, 8, -9, -10, 11, -12, -13, -14, -15, 16]
# Using a list comprehension, create a new list from [1, 2, 3, -4, -5, 6] that contains only the positive numbers.
positiveList = [num for num in ls if num > 0]
print(positiveList)

# Write a program that categorizes numbers in a list as "Even", "Odd", or "Prime" using if-elif inside a loop.
from homework6 import isPrime

for num in ls:
    if isPrime(num):
        print(f"{num} is Prime")
    elif num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Create a nested list comprehension to generate a multiplication table (1-10).
multiplicationTable = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in multiplicationTable:
    print(row)

# Write a program to filter and print words from a list of strings that start with vowels using list comprehension.
words = ["apple", "banana", "orange", "umbrella", "grape"]
vowelWords = [word for word in words if word[0].lower() in "aeiou"]
print(vowelWords)


# Write a function calculate_average that takes any number of numerical arguments and returns their average.
def calculateAverage(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All arguments must be numbers.")
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


# Create a function all_greater that takes a list and a number as arguments and checks if all elements in the list are greater than the number.
def allGreater(lst, num):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("First argument must be a list of numbers.")
    if not isinstance(num, (int, float)):
        raise ValueError("Second argument must be a number.")
    if len(lst) == 0:
        return False
    return all(x > num for x in lst)


# Write a function divide_numbers that accepts two numbers and returns their division result. Add error handling for division by zero.
def divideNumbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


# Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.
def stringClosure():
    s = ""

    def inner(action, text=""):
        if not isinstance(action, str) or not isinstance(text, str):
            raise ValueError("Both action and text must be strings.")
        nonlocal s
        if action == "append":
            s += text
        elif action == "reset":
            s = text
        return s

    return inner


string_func = stringClosure()
print(string_func("append", "Hello"))
print(string_func("append", " World"))
