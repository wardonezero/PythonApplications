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

#Implement a function make_greeting(greeting) that takes a greeting string and returns a function that takes a name and prints the greeting followed by the name.
def makeGreeting(greeting):
    def inner(name):
        print(f"{greeting}, {name}")
    return inner

makeGreeting("Hello")("John")
makeGreeting("Hi")("Jane")

#Write a function make_accumulator(start=0) that returns a function which adds its argument to start and returns the new total each time it is called.
def makeAccumulator(start = 0):
    def inner(num):
        nonlocal start
        start += num
        return start
    return inner
print(makeAccumulator(6)(8))
print(makeAccumulator(4)(5))

#Implement a function make_config(key, value) that returns a function which, when called, returns a dictionary with the given key-value pair.
def makeConfig(key, value):
    def inner():
        return {key: value}
    return inner
print(makeConfig("name", "John")())
print(makeConfig("age", 25)())