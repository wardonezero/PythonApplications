#Write a function fibonacci(n) that calculates the nth Fibonacci number without using recursion. Use an iterative approach to compute the result.
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
    
#Write a function factorial(n) that calculates the factorial of a given number using an iterative approach. 
def factorialNumber(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
print (fibonacciNth(10))
print (factorialNumber(10))
