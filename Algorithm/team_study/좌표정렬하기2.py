from sys import stdin

n = int(input())
mylist = []

for i in range(n):
    mylist.append(list(map(int, stdin.readline().split())))

mylist.sort(key=lambda x: (x[1], x[0]))

for i in mylist:
    print(i[0], i[1])

#408ms