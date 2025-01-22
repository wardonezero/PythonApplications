import math
a = 0
a += 1
a -= 2
a *= 3
a /= 4
a **= 5
remainder = 10 % 3
# print(a)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# Exercises 1
radius = float(input('Enter the radius of the circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {circumference}")

# Exercises 2

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

# Exercises 3
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2)+pow(b,2))

print(f"Side C = {c}")