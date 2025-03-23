#Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.
def printDownFromNrec(n):
    if n == 0:
        return
    print(n, end="-")
    return printDownFromNrec(n-1)

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


#Write a function print_characters(s) that prints each character of a string sss on a new line using recursion.
def printCharactersRec(s):
    if not s:
        return
    print(s[0])
    return printCharactersRec(s[1:])


#Write a function sum_up_to_n(n) that returns the sum of numbers from 1 to n using recursion.
def sumUpToN(n):
    if n == 0:
        return 0
    return n + sumUpToN(n-1)