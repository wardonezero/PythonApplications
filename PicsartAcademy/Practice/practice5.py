# Mar 30

# Extract the diagonal elements from a matrix
matrix = [[2, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_elements = []
for i in range(len(matrix)):
    diagonal_elements.append(matrix[i][i])
print("Diagonal elements:", diagonal_elements)


# Recursively extract the secondary diagonal elements’ sum  from a matrix
def secondary_diagonal_sum(matrix, row=0):
    if row == len(matrix):
        return 0
    return matrix[row][len(matrix) - row - 1] + secondary_diagonal_sum(matrix, row + 1)


print("Secondary diagonal sum:", secondary_diagonal_sum(matrix))


# Իրականացնլ ռեկուրսիվ ֆունկցիա, որը ստանում է string և վերադարձնում string-ում առաջին հանդիպած մեծատառը։
def first_uppercase(string: str) -> str:
    if not string or not isinstance(string, str):
        return None
    if string[0].isupper():
        return string[0]
    return first_uppercase(string[1:])


print("First uppercase letter:", first_uppercase("hello World"))

#Implement  a recursive function which will calculate the gcd of two numbers.
def gcd(a, b):
    # if b == 0:
    #     return a
    # return gcd(b, a % b)
    pass
