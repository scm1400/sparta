input = list(range(0, 10001))

for i in range(10001):
    sum = i
    while (i != 0):
        sum += i % 10
        i = int(i / 10)
    try:
        input.remove(sum)
    except:
        continue

for num in input:
    print(num)