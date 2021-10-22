from sys import stdin

input()
mylist = []
cmds = stdin.readlines()

for i in cmds:
    cmd = i.split()
    if (cmd[0] == 'push'):
        mylist.append(int(cmd[1]))
    elif (cmd[0] == 'pop'):
        try:
            print(mylist.pop(-1))
        except:
            print(-1)
    elif (cmd[0] == 'size'):
        print(len(mylist))
    elif (cmd[0] == 'empty'):
        if (len(mylist) == 0):
            print(1)
        else:
            print(0)
    elif (cmd[0] == 'top'):
        if (len(mylist) == 0):
            print(-1)
        else:
            print(mylist[-1])

# 84ms
