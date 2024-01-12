import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())
A = [[] for _ in range(N+1)]

## 그래프 생성 (인접 리스트)
for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)


for i in range(1, N+1):
  A[i].sort()


## DFS > 재귀
# 시작점 V와 순차적으로 연결되는 노드들

def DFS(x):
  visited[x] = True
  print(x, end=' ')
  for k in A[x]:
    if not visited[k]:
      visited[k] = True
      DFS(k)

visited = [False] * (N+1)

DFS(V) 


## BFS > 큐
# 시작점 V에 직접 연결된 노드들

def BFS(x):
  q = deque()
  q.append(x)
  visited[x] = True

  while q:
    now = q.popleft()
    print(now, end=' ')
    for i in A[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

visited = [False] * (N+1)
print()
BFS(V)
