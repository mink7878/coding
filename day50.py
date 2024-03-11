import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
result = [0] * (N+1)
A = [[] for _ in range(N+1)]

for i in range(N-1):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

#### DFS

def DFS(v):
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      result[i] = v
      DFS(i)

DFS(1)

for k in range(2, N+1):
  print(result[k])