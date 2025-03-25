# Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.
def printDownFromNrec(n):
    if n == 0:
        return
    print(n, end="-")
    return printDownFromNrec(n - 1)


def printDownFromN(n):
    for i in range(n, 0, -1):
        print(i, end="-")


# import time
# start_time = time.perf_counter()
printDownFromNrec(6)
# end_time = time.perf_counter()
# print(f"{end_time - start_time:.6f} s")

# start_time = time.perf_counter()
printDownFromN(6)
# end_time = time.perf_counter()
# print(f"{end_time - start_time:.6f} s")

print()


# Write a function print_characters(s) that prints each character of a string sss on a new line using recursion.
def printCharactersRec(s):
    if not s:
        return
    print(s[0])
    return printCharactersRec(s[1:])


# Write a function sum_up_to_n(n) that returns the sum of numbers from 1 to n using recursion.
def sumUpToN(n):
    if n == 0:
        return 0
    return n + sumUpToN(n - 1)


# Write a recursive function to calculate the factorial of a number n.
def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Create a recursive function to find the sum of the first n natural numbers.
def sumOfFirstN(n: int) -> int:
    if not n or n < 1:
        return 0
    return n + sumOfFirstN(n - 1)


# Write a recursive function to calculate the nth Fibonacci number.
def fibonacci(n: int) -> int:
    if not n or n < 1:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Write a recursive function to reverse a given string.
def reverseString(s: str) -> str:
    if not s or len(s) <= 1:
        return s
    return s[-1] + reverseString(s[:-1])


# Write a recursive function to check if a string is a palindrome.
def isPalindrome(s: str) -> bool:
    if not s or s[0] != s[-1]:
        return False
    if len(s) == 1:
        return True
    return isPalindrome(s[1:-1])


# Write a recursive function to calculate the power of a number x raised to n.
def powerOfX(x: int, n: int) -> int:
    if not n or n < 1:
        return 1
    return x * powerOfX(x, n - 1)


print(powerOfX(3, 2))


# Write a recursive function to calculate the sum of all digits in a number.
def sumOfDigits(n: int) -> int:
    if not n:
        return 0
    return n % 10 + sumOfDigits(n // 10)


# Write a recursive binary search algorithm to find the index of a target value in a sorted array.
def binarySearch(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binarySearch(arr, target, left, mid - 1)
    return binarySearch(arr, target, mid + 1, right)


# Write a recursive function to flatten a list containing nested lists.
def flattenList(arr: list) -> list:
    if not arr:
        return []
    if isinstance(arr[0], list):
        return flattenList(arr[0]) + flattenList(arr[1:])
    return [arr[0]] + flattenList(arr[1:])


# Write a recursive function to find the maximum element in a list.
def maxElement(arr: list) -> int:
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], maxElement(arr[1:]))
