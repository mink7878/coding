import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)


def BFS(v):
  visited = [False] * (N+1)
  answer = [0] * (N+1)
  q = deque()
  visited[v] = True
  q.append(v)

  while q:
    now = q.popleft()
    for i in A[now]:
      if not visited[i]:
        visited[i] = True
        answer[i] = answer[now] + 1 
        q.append(i)

  return answer

result = BFS(X)

tmp = 0
for i in range(1, N+1):
  if result[i] == K:
    tmp = i
    print(tmp)

if tmp == 0:
  print(-1)