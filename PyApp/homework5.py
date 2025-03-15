#Write a function named greet that prints "Hello, World!". Call the function. 
def greet():
    print("Hello, World!")
greet()

#Write a function add that takes two numbers as arguments and returns their sum. Call the function with different inputs.
def addTwoNumbers(a,b):
    return a + b
print(addTwoNumbers(1,7))
print(addTwoNumbers(20,20))

#Create a function multiply that takes two numbers and returns their product.
def multiplyTwoNumbers(a,b):
    return a * b

#Write a function personal_greet that takes a name as an argument and prints "Hello, [name]!".
def personal_greet(name):
    print(f"Hello, {name}!")

#Write a function calculate_area that takes length and width as parameters and returns the area of a rectangle.
def calculate_area(length, width):
    return length * width

#Write a function greet_with_message that takes a name and an optional message. The default message should be "Welcome!".
def greet_with_message(name, message = "Welcome!"):
    print(f"Hello, {name}! {message}")
greet_with_message("Alice")
greet_with_message("Bob", "Good morning!") 

#Write a function power that takes a number and an optional exponent. The default exponent should be 2 (square the number).
def power(number, exponent = 2):
    return number ** exponent
print(power(3))
print(power(3, 3))

#Write a program with a global variable x. Create a function that changes the value of x inside the function and prints both the global and local values.
x = 10
def changeX():
    global x
    x = 20
    print(x)
changeX()
print("Global x:", x)

#Write a function is_even that takes a number and returns True if the number is even and False otherwise.
def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(5))

#Write a function find_max that takes two numbers and returns the larger of the two.
def find_max(a, b):
    return a if a > b else b
print(find_max(20, 10))

#Write a function calculate_discount that takes a price and a discount percentage and returns the discounted price.
def calculate_discount(price, discount):
    return price - price * discount / 100
print(calculate_discount(100, 20))

#Write a function filter_positive that takes a list of numbers and returns a new list containing only the positive numbers.
def filter_positive(*nums):
    return [num for num in nums if num > 0]
print(filter_positive([-5, 3, -1, 2, 0]))

#Write a function count_digits that takes an integer and returns the number of digits in it.
def count_digits(number):
    return len(str(number))
print(count_digits(12345))

#Write a function sum_of_digits that calculates the sum of all digits in an integer
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
print(sum_of_digits(123))