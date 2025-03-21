# Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
def sum_numbers(*args) -> int:
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return 0


print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(1, 2, 3, 4, 5, "a"))
print(sum_numbers())


# Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
def display_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end="-")


# Write a function order_item that accepts:
# A required item argument.
# A quantity argument with a default value of 1.
# Arbitrary positional arguments (*args) to specify additional options.
# Arbitrary keyword arguments (**kwargs) for customization details.
def order_item(item: str, quantity: int = 1, *args, **kwargs) -> None:
    pass


# #Write a function register_user that accepts:
# A required positional argument: username.
# A required keyword-only argument: email.
def register_user(username, *, email):
    pass


# Analyze the following code, explain why it raises an error, and fix the function call:
def book_ticket(destination, price, discount=0, *extras, **details):
    print(f"Booking to {destination} for ${price - discount}")
    if extras:
        print(f"Extras: {', '.join(extras)}")
    if details:
        print(f"Details: {details}")


# book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)
# The error is raised because the keyword arguments should be passed after the positional arguments.
book_ticket("Paris", 100, 10, "window seat", "meal")
book_ticket("Paris", 100, 10, "window seat", "meal", **{"name": "John"})


# Implement a function process_data that accepts a mix of positional arguments, default arguments,
# arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
# Require the first two arguments to be data (a list) and operation (a string that specifies the operation to perform: 'sum', 'multiply', 'filter').
# Optionally accept a threshold parameter with a default value of None. This will only be used for the 'filter' operation.
# Accept additional numbers via *args to be appended to the data list before processing.
# Accept additional processing options through **kwargs, such as:
# reverse (boolean): Whether to reverse the result.
# unique (boolean): Whether to ensure the data list contains unique values before processing.
# Function Behavior:
# If the operation is 'sum', return the sum of the elements in the data list.
# If the operation is 'multiply', return the product of the elements in the data list.
# If the operation is 'filter', return a list of numbers greater than threshold.
# Apply reverse and unique options based on the kwargs values.
def process_data(data: list, operation: str, *args, threshold=None, **kwargs) -> list:
    data.extend(args)
    if operation == "sum":
        result = sum(data)
    elif operation == "multiply":
        result = 1
        for num in data:
            result *= num
    elif operation == "filter":
        result = [num for num in data if num > threshold]
    if kwargs.get("reverse"):
        result = result[::-1]
    if kwargs.get("unique"):
        result = list(set(result))
    return result

#Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

#Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.
def multiplier(multiplier):
    def inner(num):
        return num * multiplier
    return inner

#Write a closure that tracks the number of times a specific function is called.
def call_counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} was called {count} times")
        return func(*args, **kwargs)
    return inner


#Create a closure to calculate running totals. Each call to the inner function should add a number to the total and return the updated total.
def running_total():
    total = 0
    def inner(num):
        nonlocal total
        total += num
        return total
    return inner

#Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.
def string_processor():
    string = ""
    def inner(new_string=""):
        nonlocal string
        if new_string:
            string += new_string
        else:
            string = ""
        return string
    return inner
