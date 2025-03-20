# Write a function fibonacci(n) that calculates the nth Fibonacci number without using recursion. Use an iterative approach to compute the result.
def fibonacciNth(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for i in range(2, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2


# Write a function factorial(n) that calculates the factorial of a given number using an iterative approach.
def factorialNumber(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


print(fibonacciNth(10))
print(factorialNumber(10))


# Write a function is_prime(n) that checks if a number is a prime number using a loop. The function should return True if the number is prime and False otherwise.
def isPrime(n: int) -> bool:
    if (not isinstance(n, int) or n < 2 or n % 2 == 0) and n != 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


print(isPrime(7))
print(isPrime(2))
print(isPrime(3))
print(isPrime(6))
print(isPrime(11))


# Write a function reverse_string(s) that reverses a string without using slicing or built-in functions like reversed(). Use a loop to construct the reversed string.
def reverseString(s: str) -> str:
    reversedString = ""
    for i in s:
        reversedString = i + reversedString
    return reversedString


s1 = "Hello, World!"
print(reverseString(s1))


# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը:
def sumOfDigits(n: int) -> int:
    if not isinstance(n, int):
        return "Please enter an integer number!"
    return sum(int(i) for i in str(n) if i.isdigit())


print(sumOfDigits(-123))

# def sum_of_digits(n: int = -124) -> int:
#     sum = 0
#     n = abs(n)
#     while n > 0:
#         sum += n % 10
#         n = n // 10
#     return sum
# print(sum_of_digits())


# Իրականացնել int տիպի արժեք վերադարձնող ֆունկցիա, որը վերադարձնում է՝ 1, եթե ֆունկցային փոխանցված ամբողջ թիվը կարող է արտահայտվել երկու պարզ թվերի գումարով, հակառակ դեպքում ֆունկցիան կվերադարձնի՝ 0:
def isSumOfTwoPrimes(n: int) -> int:
    pass


print(isSumOfTwoPrimes(10))


# Իրականացնել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  def power (num: int, exp:int): Ֆունկցիան վերադարձնում է num ամբողջ թվի exp աստիճանի արժեքը։
def power(num: int, exp: int) -> int:
    if not isinstance(num, int) or not isinstance(exp, int):
        return "Please enter an integer number!"
    return num**exp


print(power(2, 4))


# Մուտքագրել թիվ, տպել թվի թվանշանները առանձին առանձին էկրանին։ Օրինակ՝ մուտքագրված 5479 թվի համար տպել ‘5’, ‘4’, ‘7’, ‘9’։
def printDigits(n: int):
    if not isinstance(n, int):
        return "Please enter an integer number!"
    for i in str(n):
        print(i, end=" ")


printDigits(5479)
