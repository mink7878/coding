### 시간초과 >>> 관점 바꾸기 + PyPy

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  A[b].append(a)

print(A)

def BFS(v):
  q = deque()
  q.append(v)

  visited = [False] * (N+1)
  visited[v] = True

  cnt = 1
  
  while q:
    now = q.popleft()
    for i in A[now]:
      if not visited[i]:
        visited[i] = True
        cnt += 1
        q.append(i)
        
  return cnt


answer = []
for i in range(N+1):
  answer.append(BFS(i))

maxVal = max(answer)
for i in range(1, N+1):
  if answer[i] == maxVal:
    print(i, end=' ')