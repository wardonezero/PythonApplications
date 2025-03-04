# str_input = 'abcabcbb'
# longest = ''
# for i in range(len(str_input)):
#     for j in range(i, len(str_input)):
#         if len(str_input[i:j]) > len(longest) and len(set(str_input[i:j])) == len(str_input[i:j]):
#             longest = str_input[i:j]
# print(longest)

str = 'abcabcbbdump'
longest = ''
for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        print(j)
        if len(str[i:j]) > len(longest) and len(set(str[i:j])) == len(str[i:j]):
            longest = str[i:j]
        
print(len(str))
print(longest)

print(str[11:12])
print(str[0:0])