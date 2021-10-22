num = int(input())

new_num = 0
temp = num
cnt = 0

while True:
    cnt += 1
    new_num = (temp % 10 * 10) + (temp % 10 + temp//10) % 10
    temp = new_num
    print(new_num)
    if new_num == num:
        break

print(cnt)

# 72ms
