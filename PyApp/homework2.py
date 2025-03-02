list = []

def AddElements():
    elements = input('Enter the element(s) you want to add separated by space:\n').split()
    if len(elements) == 1:
        list.append(elements)
    else:
        list.extend(elements)

def InsertElement():
    index = int(input('Enter the index of the element where you want to insert the new element: '))
    if index > len(list):
        print('Index out of range')
    else:
        element = input('Enter the element you want to insert')
        list.insert(index, element)

def RemoveElement():
    choice = input('Enter I to remove by index or E to remove by element: ')
    if choice == 'I':
        index = int(input('Enter the index of the element you want to remove: '))
        if index > len(list):
            print('Index out of range')
        else:
            list.pop(index)
    elif choice == 'E':
        element = input('Enter the element you want to remove: ')
        if element not in list:
            print('Element not found')
        else:
            list.remove(element)
    else:
        print('Invalid choice')
    

print('You have empty list')
AddElements()
print('Your list is:', list)
InsertElement()
print('Your list is:', list)
RemoveElement()
print('Your list is:', list)



#Write a program to create a list and a tuple with some elements. Print them and display their types.
alist = [1, 2, 3, 4, 5, 3, 3]
atuple = (1, 2, 3, 4, 5, 3, 3)
print(f'Type of List is {type(alist)} and Type of Tuple is {type(atuple)}')

#Write a program to count the occurrences of a specific element in a list and tuple.
print(f'Count of 3 in list is {alist.count(3)} and Count of 3 in tuple is {atuple.count(3)}')

#Write a program to find and print the maximum and minimum values in a list and a tuple.
print(f'Maximum value in list is {max(alist)} and Minimum value in list is {min(alist)}')

#Write a program to access elements from a nested list and a nested tuple.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_list[1][2])
print(nested_tuple[1][2])

#Write a program to find the sum of all elements in a list and a tuple.
print(f'Sum of all elements in list is {sum(alist)} and Sum of all elements in tuple is {sum(atuple)}')

#Write a program to reverse a list and a tuple.
print(f'Reversed list is {alist[::-1]} and Reversed tuple is {atuple[::-1]}')
# alist.reverse()
# reversed(alist)

#Create a program that adds, subtracts, multiplies, and divides two integers, two floats, and a combination of both.
a = 11 
b = 4
c = 4.11
d = 2.44
print(f'Addition of {a} and {b} is {a + b}')
print(f'Subtraction of {a} and {b} is {a - b}')
print(f'Multiplication of {a} and {b} is {a * b}')
print(f'Division of {a} and {b} is {a / b}')
print(f'Addition of {c} and {d} is {c + d}')
print(f'Subtraction of {c} and {d} is {c - d}')
print(f'Multiplication of {c} and {d} is {c * d}')
print(f'Division of {c} and {d} is {c / d}')
print(f'Addition of {a} and {c} is {a + c}')
print(f'Subtraction of {a} and {c} is {a - c}')
print(f'Multiplication of {a} and {c} is {a * c}')
print(f'Division of {a} and {c} is {a / c}')


#Write a program to calculate the product of two complex numbers.
a = 3 + 4j
b = 5 + 6j
print(f'Product of {a} and {b} is {a * b}')

#Create a fraction that represents 1/2 and another fraction representing 2/3. Add them and print the result.
from fractions import Fraction
a = Fraction(1, 2)
b = Fraction(2, 3)
print(f'Sum of {a} and {b} is {a + b}')

#Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(f'Sum of {a} and {b} is {a + b}')
print(f'Sum of 0.1 and 0.2 is {0.1 + 0.2}')

#Write a program to check if the sum of three numbers is equal to 100. Use boolean comparisons to print the result as True or False.
a = 16
b = 32
c = 64
print(a + b + c == 100)

#Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them.
#Use the fractions.Fraction class to handle fractions and print the resulting fraction in its simplified form.
a = input('Enter the first fraction in the form of a/b: ')
b = input('Enter the second fraction in the form of a/b: ')
a = Fraction(a)
b = Fraction(b)
print(f'')

#Accept two fractions from the user and find their GCD using the math.gcd() function along with the numerator and denominator attributes of each fraction.
import math
a = input('Enter the first fraction in the form of a/b: ')
b = input('Enter the second fraction in the form of a/b: ')
a = Fraction(a)
b = Fraction(b)
gcd = math.gcd(a.numerator, a.denominator)

#Write a program to check if a number is even or odd.
a = int(input('Enter a number: '))
if a % 2 == 0:
    print('Even')
else:
    print('Odd')

#Compare the values of a float and an int and print whether they are equal or not.
a = 8
b = 16.1
if a == b:
    print('Equal')
else:
    print('Not Equal')

#Calculate the square of an integer and a float using the exponentiation operator (**).
a = 2
b = 4.1
print(f'Square of {a} is {a ** 2} and Square of {b} is {b ** 2}')

#Write a program to find the maximum of three numbers using nested conditional operators.
a = 8
b = 16
c = 32
print(a if a > b and a > c else b if b > c else c)


#Accept two integer inputs from the user and calculate the absolute difference between them using the abs() function. Print the result.
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(f'absolute difference is {abs(a - b)}')

#Accept an integer input from the user and use conditional statements to print whether the number is positive, negative, or zero.
a = int(input('Enter a number: '))
if a > 0:
    print('Positive')
elif a < 0:
    print('Negative')
else:
    print('Zero')

#Accept two integer inputs from the user. Check if the first number is a multiple of the second and print True if it is, otherwise print False.
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(f'the first number is a multiple of the second: {a % b == 0}')