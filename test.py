from math import sqrt
def isPrime(n: int) -> bool:
    if (not isinstance(n, int) or n < 2 or n % 2 == 0) and n != 2:
        return False
    # for i in range(3, n//2, 2):
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


for i in range(1, 100):
    if isPrime(i):
        print(i, end=" ")
print()
