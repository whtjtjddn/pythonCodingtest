import sys

input=sys.stdin.readline

num = int(input())

string = []

for i in range(0,num):
    str = input()
    string = list(str)
    left = 0
    right = 0
    flag = 0

    for j in range(0,len(string)-1):
        if left == 0 & right == 0:
            if string[j] == ')':
                print("NO")
                flag = 2
                break
        
        if string[j] == '(':
            left = left + 1
        else:
            right = right + 1
            
        if left == right:
            left = 0
            right = 0
            flag = 0
        else:
            flag = 1

    if flag == 0:
        print("YES")
    elif flag == 2:
        continue
    else:
        print("NO")
