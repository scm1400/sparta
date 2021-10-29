n, m = map(int, input().split())
s = list(map(int ,input().split()))
mylist = list(range(1, n + 1))
cnt = 0
for i in range(m):
    mylist_len = len(mylist)
    mylist_index = mylist.index(s[i])
    if mylist_index < mylist_len - mylist_index:
        while True:
            if mylist[0] == s[i]:
                del mylist[0]
                break
            else:
                mylist.append(mylist[0])
                del mylist[0]
                cnt += 1
    else:
        while True:
            if mylist[0] == s[i]:
                del mylist[0]
                break
            else:
                mylist.insert(0, mylist[-1])
                del mylist[-1]
                cnt += 1
print(cnt)