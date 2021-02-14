import sys

input=sys.stdin.readline

stack = []

num = int(input())

for i in range(0,num):
    str = input().split()
    
    if str[0] == "push":
        push = int(str[1])
        stack.append(push)
        
    elif str[0] == "pop":
        n = len(stack)
        if n == 0:
            print(-1)
        else:
            pop = stack.pop()
            print(pop)
    elif str[0] == "top":
        n = len(stack)
        if n == 0:
            print(-1)
        else:
            top = stack[-1]
            print(top)
    elif str[0] == "size":
        n = len(stack)
        print(n)
    elif str[0] == "empty":
        n = len(stack)
        if n == 0:
            print(1)
        else:
            print(0)
