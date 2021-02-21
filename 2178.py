from sys import stdin

n,m = map(int, stdin.readline().split())

matrix = [stdin.readline().rstrip() for _ in range(n)]

visited = [[0]*m for _ in range(n)]


cnt = 0

queue = [(0,0)]
visited[0][0] = 1

while queue:
    x,y = queue.pop(0)
    
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break

    else:
        dx = x - 1
        dy = y
        if 0<=dx<n and 0<=dy<m:
            if visited[dx][dy] == 0 and matrix[dx][dy] == '1':
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx,dy))
                
        dx = x + 1
        dy = y
        if 0<=dx<n and 0<=dy<m:
            if visited[dx][dy] == 0 and matrix[dx][dy] == '1':
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx,dy))
        dx = x
        dy = y - 1
        if 0<=dx<n and 0<=dy<m:
            if visited[dx][dy] == 0 and matrix[dx][dy] == '1':
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx,dy))
                
                    
        dx = x
        dy = y + 1
        if 0<=dx<n and 0<=dy<m:
            if visited[dx][dy] == 0 and matrix[dx][dy] == '1':
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx,dy))
        
