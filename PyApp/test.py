str = 'abcabcbbdump'
longest = ''
for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        if len(str[i:j]) > len(longest) and len(set(str[i:j])) == len(str[i:j]):
            print(set(str[i:j]))
            longest = str[i:j]
        
print(longest)