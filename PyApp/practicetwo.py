ls = [1,2,4,3]
result = 0
for i in range(1, len(ls)):
    if ls[i] > result:
        result = ls[i]
print(result)

min_value = 0
min_index = 0
for i in range(1, len(ls)):
    if ls[i-1] < min_value:
        min_value = ls[i-1]
        min_index = i-1
print(min_index)

ls1 = [1,2,3,4,5]
ls2 = [6,7,8,9,10]
for i in range(len(ls1)):
    print(ls1[i] * ls2[i])

a = int(input('Enter the normal number: '))
if a in ls:
    print('YES')
else:
    print('NO')

lsstr = ['ab','cd','ef','gh','ij','kl','mn','op','qr','st','uv','wx','yz']
for i in range(len(lsstr)):
    if lsstr[:i].count(lsstr[i]) >= 1:
        continue
    print(f'{lsstr[i]}: {lsstr.count(lsstr[i])}')

