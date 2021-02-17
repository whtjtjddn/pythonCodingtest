from collections import deque
import sys

input=sys.stdin.readline

n,k = input().split()

n = int(n)
k = int(k)

x = 0
tmp = 0
tmp1 = 0
data = deque([])
data1 = deque([])

for i in range(1,n+1):
    data.append(i)



while len(data1) != n:

    tmp = x
    
    while tmp1 != k:
         
        if data[tmp] != 0:
            tmp1 = tmp1 +1
            tmp = tmp+1
        else:
            tmp = tmp+1
        if tmp >= n:
            tmp = tmp - n
           
    x = tmp
    
    if data[x-1] != 0:
        data1.append(data[x-1])
        data[x-1] = 0
        tmp1 = 0
    else:
        data1.append(data[x-1])
        tmp1 = 0
        continue
print('<',end = '')
for i in range(0,len(data1)):
    if i == len(data1)-1:
        print(data1[i],end = '')
        break
    print(data1[i], end = ', ')
print('>')
