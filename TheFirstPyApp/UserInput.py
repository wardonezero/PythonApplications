# User input
name = input('What is your name? Enter your name: ')
print(f'Welcome {name}')
age = input('How old are you? Enter your age: ')
if int(age) > 18:
    print('You allowed to continue')
    # mad libs game
    adjective = input('Enter an adjective: ')
    verb = input('Enter a verb, past tense: ')
    noun = input('Enter a noun: ')
    food = input('Enter a food: ')
    adjective = input('Enter an adjective: ')
    emotion = input('Enter an emotion: ')
    print('Whole story')
    print(f'It was a {adjective} day at the beach.')
    print(f'We {verb} in the {noun} and ate {food}.')
    print(f'The sun was {adjective} and we felt {emotion}. Best day ever!')
else:
    print('You are not allowed to continue')

# area calculator
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

area = length * width
volume = length * width * height
print(f"The area is: {area}cm^2")
print(f"The volume is: {volume}cm^3")

# shopping cart
item = input("What item would you like to buy ?: ")
price = 0
for i in item:
    price += ord(i)
quantity = int(input("How many would you like ?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
total = total * 1.02
print(f"Your total is: ${round(total, 2)}")
print(total)