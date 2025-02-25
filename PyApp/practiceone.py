import fractions
import decimal

#1. Write a Python program that asks a user for two numbers and prints their sum.
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print(f'{first} + {second} = ',first + second)

#2 Create two integer variables and perform addition, subtraction, multiplication, and division.
#2.1 Repeat the same for two floating-point numbers.
#2.2 Repeat the same for complex numbers.

a = 1 
b = 2

print(f'{a} * {b}: {a * b}')
print(f'{b} / {b}: {b / b}')
print(f'{a} + {b}: {a + b}')
print(f'{b} + {a}: {b + a}')

a = 1.3
b = 2.2

print(f'{a} * {b}: {a * b}')
print(f'{b} / {b}: {b / b}')
print(f'{a} + {b}: {a + b}')
print(f'{b} + {a}: {b + a}')

a = 1.34
b = 2.2j

print(f'{a} * {b}: {a * b}')
print(f'{b} / {b}: {b / b}')
print(f'{a} + {b}: {a + b}')
print(f'{b} + {a}: {b + a}')

#3 Create and Compare Numbers of Different Types
#3.1 Compare an integer and a float
#3.2 Compare a decimal and a float
#3.3 Compare two fractions
#5 Create examples to compare two numbers using all relational operators
#(>, <, ==, !=, >=, <=). Write down the results for different types of numbers.

a = 1
b = 1.1
c = decimal.Decimal(1.12)
d = fractions.Fraction(1.13)
e = fractions.Fraction(1, 2)

print(f'{a} == { b}: {a == b}')
print(f'{a} != { b}: {a != b}')
print(f'{a} <= { b}: {a <= b}')
print(f'{a} >= { b}: {a >= b}')
print(f'{a} > {b}: {a > b}')
print(f'{a} < {b}: {a < b}')

print(f'{c} == {b}: {c == b}')
print(f'{c} != {b}: {c != b}')
print(f'{c} <= {b}: {c <= b}')
print(f'{c} >= {b}: {c >= b}')
print(f'{c} <1 {b}: {c < b}')
print(f'{c} >1 {b}: {c > b}')

print(f'{d} == {e}: {d == e}')
print(f'{d} != {e}: {d != e}')
print(f'{d} <= {e}: {d <= e}')
print(f'{d} >= {e}: {d >= e}')
print(f'{d} < {e}: {d < e}')
print(f'{d} > {e}: {d > e}')


#4  Create Complex Numbers and Calculate Magnitude
#Formula |z| = \sqrt{a^2 + b^2}
firstComplexNumber = 2 + 4j
secondComplexnumber = 1 - 1j

firstComplexNumber_magnitude = (firstComplexNumber.real**2 + firstComplexNumber.imag**2)**0.5
secondComplexnumber_magnitude = (secondComplexnumber.real**2 + secondComplexnumber.imag**2)**0.5
#or
import math
firstComplexNumber_magnitude = math.sqrt(firstComplexNumber.real**2 + firstComplexNumber.imag**2)
secondComplexnumber_magnitude = math.sqrt(secondComplexnumber.real**2 + secondComplexnumber.imag**2)
#or
firstComplexNumber_magnitude = abs(firstComplexNumber)
secondComplexnumber_magnitude = abs(secondComplexnumber)

# Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.
# Create a decimal number and experiment with adding or subtracting very small decimal values.

a = fractions.Fraction(0.1)
b = fractions.Fraction(0.2)
print('manually: 0.1 + 0.2 = 0.3')
print(f'{a} + {b}: {a + b}')
print('manually: 0.1 - 0.2 = -0.1')
print(f'{a} - {b}: {a - b}')
print('manually: 0.1 * 0.2 = 0.02')
print(f'{a} * {b}: {a * b}')
print('manually: 0.1 / 0.2 = 0.5')
print(f'{a} / {b}: {a / b}')

a = decimal.Decimal(0.1)
b = decimal.Decimal(0.2)
print(f'{a} + {b}: {a + b}')

#6 Create two separate strings and then concatenate them together.
# Have them experiment with adding a space between the words.

a = 'hello'
b = 'world'
c = 'a'+ 'b'
c = 'a'+ '    '+ 'b'

#7 Write a program that takes a string and extracts the first and last character using subscripts (indexing).
someText = input('Enter some text: ')
print(f'the first letter is {someText[0]} and the last letter is {someText[-1]}')

#8 Write a program that slices the first 3 characters and the last 2 characters from a string.
someText = 'idk what to write'
slicedText = someText[3:-2]
print(f'Sliced text: {slicedText}')
# print(f'the first three letters are {someText[:3]} and the last two letters are {someText[-2:]}')

#9 Write a program that takes two strings as input and concatenates them with a space in between.
firstText = input('Enter the first text: ')
secondText = input('Enter the second text: ')
result = firstText +' ' + secondText
print(result)

#10 Write a program that takes a string and converts it to both uppercase and lowercase.
print(someText.upper())
print(someText.lower())

#11 Write a program that checks whether a string starts with the letter "A" and ends with the letter "Z".
print(f'The first letter is A: {someText[0]=='A'}')
print(f"The last letter is Z: {someText[-1]=='Z'}")

#12 Write a program that counts how many times the letter "a" appears in a given string.
banana = 'banana'
print(banana.count('a'))

#13 Write a program that takes a sentence and splits it into words, then joins the words back into a sentence with hyphens (-) between them.
sentence = input('Enter a sentence: ')
words = sentence.split(' ')
print('-'.join(words))

#14 Write a program that takes a user’s name as input and creates a greeting message like "Hello, [Name]!".
name = input('Enter your name: ')
print(f'Hello, {name}!')