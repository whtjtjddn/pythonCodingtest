from collections import deque
import sys

input=sys.stdin.readline

class myGraph:
  def __init__(self):
    self.graph = {}

  def addInfo(self, startV, endVs):
    self.graph[startV] = endVs
  def bfs(self, startV):
    q = deque([startV])
    visited = [startV]
    while q:
      nowV = q.popleft()
      for nextV in range(len(matrix[startV])):
        if matrix[nowV][nextV] == 1 and nextV not in visited:
          q.append(nextV)
          visited.append(nextV)
    return visited

  def dfs(self, startV, visited):
    visited += [startV]
    for nextV in range(len(matrix[startV])):
      if matrix[startV][nextV] and nextV not in visited:
        g.dfs(nextV,visited)
    return visited

g = myGraph()

v,n,s = input().split()
v = int(v)
n = int(n)
s = int(s)
cnt = 0
matrix = [[0]*(v+1) for _ in range(v+1)]


while cnt != n:
    start, end = input().split()
    start = int(start)
    end = int(end)
    matrix[start][end]= 1
    matrix[end][start] = 1
    cnt = cnt+1

print(*g.dfs(s,[]))
print(*g.bfs(s))
