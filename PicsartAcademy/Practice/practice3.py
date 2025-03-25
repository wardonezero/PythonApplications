# Գրել ֆունկցիա, որը կվերադարձնի [1-200] միջակայքի բոլոր զույգ թվերը:
def even_numbers() -> list:
    return [i for i in range(1, 201) if i % 2 == 0]


print(even_numbers())


# Գրել ֆունկցիա, որը կտպի տրված թվի բազմապատկման աղյուսակը։
def multiplication_table(n: int = 5) -> None:
    if isinstance(n, int):
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")
    else:
        print("Please enter an integer number!")


multiplication_table()


# Գրել ֆունկցիա, որը ստանում է n ամբողջ թիվը և վերադարաձնում մինչև [1, n] բոլոր պարզ թվերը:
def prime_numbers(n: int) -> list:
    pass


print(prime_numbers(20))


# Գրել ֆունկցիա, որը կստանա թիվ և կվերադարձնի թվի երկուական տեսքը տողի տեսքով։
def binary_number(n: int) -> str:
    if not isinstance(n, int):
        return "Please enter an integer number!"
    else:
        signBit = 0 if n >= 0 else 1
        n = abs(n)
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2
        if len(binary) < 64:
            binary = "0" * (64 - len(binary)) + binary
        if signBit == 1:
            neg = ""
            for i in binary:
                if i == "0":
                    neg += "1"
                else:
                    neg += "0"
            for i in range(len(neg) - 1, -1, -1):
                if neg[i] == "1":
                    neg = neg[:i] + "0" + neg[i + 1 :]
                else:
                    neg = neg[:i] + "1" + neg[i + 1 :]
                    break
            binary = neg
        return binary


print(binary_number(4))
print(binary_number(-4))
print(binary_number(8))
print(binary_number(-6))


# Գրել ֆունկցիա, որը կստանա նախադասություն և կվերադարձնի նրա ամենաերկար բառը։
def longest_word(sentence: str) -> str:
    if isinstance(sentence, str):
        return max(sentence.split(), key=len)
    else:
        return "Please enter a string!"


print(longest_word("This is a sentence"))


# Գրել ֆունկցիա, որը ստանում է ամբողջ թվային պարամետր: Ֆունկցիան վերադարդձնում է True՝ եթե այն կատարյալ թիվ է և False հակառակ դեպքում:
from math import sqrt


def isPerfectNumebr(n: int) -> bool:
    if n < 6 or n % 2 != 0:
        return False
    sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if i * i != n:
                sum += i + n // i
            else:
                sum += i
    return sum == n


print(isPerfectNumebr(5))


# Գրել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  int sqrt (int num); Ֆունկցիան վերադարձնում է num ամբողջ թվի քառակուսային արմատի արժեքը։
def sqrtNum(num: int) -> int:
    if isinstance(num, int):
        return num**0.5
    else:
        return "Please enter an integer number!"


print(sqrtNum(16))


# Իրականացնել join ֆունկցիան:
def myJoin(firstString: str, *strings) -> str:
    # for string in strings:
    #     firstString += string
    # return firstString
    pass


print(myJoin("Hello", " ", "world", "!"))


# Իրականացնել contain ֆունկցիան:
def contain(theString: str, aSubstring: str) -> bool:
    # return substring in string
    if len(theString) < len(aSubstring):
        return False
    for i in range(len(theString) - len(aSubstring) + 1):  # hello lo + 1  = 2
        if theString[i : i + len(aSubstring)] == aSubstring:
            return True
    return False
