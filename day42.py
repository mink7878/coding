## 최단경로 + 양수간선 >>> 다익스트라
## 우선순위 큐
## K 번째 걸리는 시간 알기 위해서는 

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

distance = [[INF] * K for _ in range(N+1)]


pq = [(0, 1)] # [[0, 1]] 가능 # 가중치 우선
distance[1][0] = 0

while pq:
  now_c, now_node = heapq.heappop(pq)
  for next_node, next_c in graph[now_node]:
    total = now_c + next_c
    if distance[next_node][K-1] > total: # 신규 경로 더 작으면 업데이트
      distance[next_node][K-1] = total
      distance[next_node].sort() # 업데이트 되면 해당 노드의 distance 배열 정렬
      heapq.heappush(pq, (total, next_node))


# print(distance)
for i in range(1, N+1):
  if distance[i][K-1] == INF:
    print(-1)
  else:
    print(distance[i][K-1])