input = 'Mississipi'

# input().upper
# set(word)
# word.count(i)

dic = dict()

for char in input:
    order = ord(char)
    if order <= 90:
        char = chr(order + 32)
    try:
        dic[char] += 1
    except:
        dic[char] = 1

# print(dic)

max_key = max(dic, key=dic.get)
# print(max_key)
max_value = dic.get(max_key)

cnt = 0
for i in dic.values():
    if i == max_value:
        cnt += 1

if cnt>1:
    print('?')
else:
    print(max_key.upper())


