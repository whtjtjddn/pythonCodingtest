from collections import deque
import sys

input=sys.stdin.readline

stack = []
strstack = []
queue = deque([])

cnt = 0

n = int(input())

for i in range(1,n+1):
    queue.append(i)
    
x = 0
maximum = 0
tmp = 0
tmp1 = 0
flag = 0
flag1 = 0

while cnt != n:
    
    x = int(input())
    
    
    if maximum<x:
        tmp1 = maximum
        maximum = x
        if flag == 0 and tmp1 != 0:
            stack.pop()
            strstack.append('-')
        for i in range(tmp1, x):
            pop = queue.popleft()
            stack.append(pop)
            strstack.append('+')
            flag = 0
        
        
    else:
        
        if x>tmp and x<maximum:
            flag1 = 1
            break
        else:
            flag = 1
            pop = stack.pop()
            strstack.append('-')
            while 1:
                if pop == x:
                    break
                else:
                    pop = stack.pop()
                    strstack.append('-')
    tmp = x
    cnt = cnt+1
if flag1 == 1:
    print("NO")
else:
    if flag == 0:
        strstack.append('-')
    
    for i in range(0,len(strstack)):
        print(strstack[i])
