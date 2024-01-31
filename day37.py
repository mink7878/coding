## 위상정렬 >>> 순서, 진입차수 리스트

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)] # 그래프
indegree = [0] * (N+1) # 진입차수 리스트

for _ in range(M):
  a, b = map(int, input().split())
  A[a].append(b)
  indegree[b] += 1

q = deque()

for i in range(1, N+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  print(now, end = ' ')
  for i in A[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      q.append(i)