# Write a Python function chain_sum that allows numbers to be added sequentially by calling the function multiple times,
# each time passing a number. The function should return itself when a number is provided, allowing an indefinite chain of calls.
# When called without arguments, it should return the accumulated sum.
# The function should start with an initial sum of 0.
# If a number is provided, the function should add it to the accumulated sum and return itself.
# If called with no arguments, it should return the accumulated sum.
def chainSum(n = 0):
    def inner(m = 0):
        return chainSum(n + m) if m else n
    return inner
    

print(chainSum()(1)(2)(3)(4)()) 
print(chainSum()(5)(10)(-2)())   
print(chainSum()(100)())         
print(chainSum()())              


#Իրականացնել ռեկուրսիվ ֆունկցիա, որը կստանա string և կվերադարձնի string-ի երկարությունը։
def stringLength(s: str) -> int:
    if not s:
        return 0
    return 1 + stringLength(s[1:])