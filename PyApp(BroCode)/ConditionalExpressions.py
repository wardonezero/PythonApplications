num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")
print("EVEN" if num % 2 == 0 else "ODD")
print(a if a > b else b)
print(a if a < b else b)
print("Adult" if age >= 18 else "Child")
print("HOT" if temperature > 20 else "COLD")
print("Full Access" if user_role == "admin" else "Limited Access")