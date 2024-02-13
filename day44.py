## 플로이드 워셜 : 모든 쌍 간의 최단거리 구하기
## 점화식 >>> Ck의 모든 값은 Ck-1에만 의존 >>> 반복 DP
## 3중 for문을 사용하기 때문에 O(V^3)

import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for x in range(1, N+1):
  for y in range(1, N+1):
    if x == y:
      graph[x][y] = 0
      break

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, N+1):
  for a in range(1, N+1):
    for b in range(1, N+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
  for b in range(1, N+1):
    if graph[a][b] == INF:
      print('INFINITY')
    else:
      print(graph[a][b], end=' ')

  print()