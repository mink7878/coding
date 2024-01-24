from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  A[a].append(b)


def BFS(v):
  q = deque()
  q.append(v)
  visited[v] = True
  
  while q:
    now = q.popleft()
    for i in A[now]:
      if not visited[i]:
        visited[i] = True
        answer[i] += 1 ### 다른점
        q.append(i)


for i in range(1, N+1):
  visited = [False] * (N+1)
  BFS(i)


for i in range(1, N+1):
  if answer[i] == max(answer):
    print(i, end=' ')