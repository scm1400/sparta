n = int(input())
count = 0
stack = []
result = []
possible = True

for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == x:
        stack.pop(-1)
        result.append("-")
    else:
        possible = False
        break

if possible == False:
    print("NO")
else:
    for i in result:
        print(i)
