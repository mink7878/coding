
import sys
INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
  graph[i][i] = 0

for _ in range(M):
  A, B = map(int, input().split())
  graph[A][B] = 1
  graph[B][A] = 1

for k in range(1, N+1):
  for s in range(1, N+1):
    for e in range(1, N+1):
      if graph[s][e] > graph[s][k] + graph[k][e]:
        graph[s][e] = graph[s][k] + graph[k][e]

mini = INF
ans = -1

for i in range(1, N+1):
  tmp = 0
  for j in range(1, N+1):
    tmp += graph[i][j]
  if mini > tmp:
    mini = tmp
    ans = i

print(ans)