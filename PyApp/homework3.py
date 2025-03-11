#Create a program that extracts the first 5 characters from a given string.
st = 'first 5 characters'
print(st[:5])

#Extract the last 3 characters of a string using slicing.
print(st[-3:])

#Write a program to print every second character from a string.
print(st[1::2])

#Reverse a given string using slicing and print the result.
print(st[::-1])

#Replace all occurrences of a specific character with another character in a string
print(st.replace('a', 'b'))

#Write a program to print a formatted message like: "Hello, my name is James and I am 20 years old." using f-strings.
name = 'James'
age = 20
print(f'Hello, my name is {name} and I am {age} years old.')

#Create a program to format and print a float with 2 decimal places.
f = 4.22224
print(f'{f:.2f}')

#Write a program to convert all characters in a string to uppercase and then to lowercase.
print(st.upper())
print(st.lower())

#Create a program to count the number of occurrences of a specific character in a string.
print(st.count('b'))

#Write a program to concatenate two strings with a space in between.
st2 = 'second string'
print(st + ' ' + st2)

#Create a program to find the sum of the first and last digit of a given number.
num = 12345
print(int(str(num)[0]) + int(str(num)[-1]))

#Write a program to calculate the average of 3 float numbers and format the result to 3 decimal places.
f1 = 1.1
f2 = 2.2
f3 = 3.3
print(f'{(f1 + f2 + f3) / 3:.3f}')

#Create a program that takes a string input and an integer input and repeats the string that many times.
str_input = input('Enter some text: ')
int_input = int(input('Enter a number: '))
print(str_input * int_input)

#Ask the user to enter a string, and then print the string in reverse order.
str_input = input('Enter some text: ')
print(str_input[::-1])

#Count how many vowels are in the string and print the count.

#Write a program that takes a string as input and outputs the longest substring without repeating characters.
str = 'abcabcbbdump'
longest = ''
for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        if len(str[i:j]) > len(longest) and len(set(str[i:j])) == len(str[i:j]):
            longest = str[i:j]
        
print(longest)

#Write a program using a while loop that repeatedly asks the user to input a number until they input 0, then print the sum of all entered numbers.
total = 0
while True:
    num = int(input('Enter a number enter 0 to stop: '))
    if num == 0:
        break
    total += num
print(total)

#Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.
ls = [1,2,3,4,5,6,7,8,9,10]
for i in ls:
    total += i
print(total)

#Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը: List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:
ls = [1,2,4,3]
result = 0
for i in range(1, len(ls)):
    if ls[i] > result:
        result = ls[i]
print(result)

#Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։
min_value = 0
min_index = 0
for i in range(1, len(ls)):
    if ls[i-1] < min_value:
        min_value = ls[i-1]
        min_index = i-1
print(min_index)

#Հայտարարել  երկու ամբողջ թվային արժեքներով list- եր  և տպել համապատասխանող ինդեքսներով էլեմնետների արտադրյալը էկրանին:
ls1 = [1,2,3,4,5]
ls2 = [6,7,8,9,10]
for i in range(len(ls1)):
    print(ls1[i] * ls2[i])

#Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։ 
a = int(input('Enter the normal number: '))
if a in ls:
    print('YES')
else:
    print('NO')

#Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում: 
lsstr = ['ab','cd','ef','gh','ij','kl','mn','op','qr','st','uv','wx','yz']
for i in range(len(lsstr)):
    if lsstr[:i].count(lsstr[i]) >= 1:
        continue
    print(f'{lsstr[i]}: {lsstr.count(lsstr[i])}')
