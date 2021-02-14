from collections import deque
import sys

input=sys.stdin.readline

data = deque([])

num = int(input())

for i in range(0,num):
    str = input().split()
    
    if str[0] == "push":
        push = int(str[1])
        data.append(push)
        
    elif str[0] == "pop":
        n = len(data)
        if n == 0:
            print(-1)
        else:
            pop = data.popleft()
            print(pop)
    elif str[0] == "front":
        n = len(data)
        if n == 0:
            print(-1)
        else:
            top = data[0]
            print(top)
    elif str[0] == "back":
        n = len(data)
        if n == 0:
            print(-1)
        else:
            top = data[n-1]
            print(top)
    elif str[0] == "size":
        n = len(data)
        print(n)
    elif str[0] == "empty":
        n = len(data)
        if n == 0:
            print(1)
        else:
            print(0)
