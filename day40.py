## 다익스트라 >>> 양수 에지 + 최단 경로 + !우선순위 큐!
### 일반 큐 써도 결과 같지만, 속도에 이점이 있음
### 우선순위 큐 : 최소 거리로 정렬된 순서로 큐에서 추출
## 최단거리 리스트 / 방문 리스트

import sys
from queue import PriorityQueue

INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())  # 노드 개수 / 에지 개수
K = int(input())  # 출발 노드

distance = [INF] * (V + 1)
visited = [False] * (V + 1)
A = [[] for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  A[u].append((v, w))

pq = PriorityQueue()

pq.put((0, K)) # 앞 : stacked 기준 / 뒤 : 노드
distance[K] = 0

while pq.qsize() > 0: ## 우선순위 큐는 "while q:" 아님
  now = pq.get()
  now_node = now[1]
  
  if visited[now_node]:
    continue
  visited[now_node] = True
  
  for next in A[now_node]:
    next_node = next[0]
    next_edge = next[1]
    if not visited[next_node]:
      if distance[next_node] > distance[now_node] + next_edge:
        distance[next_node] = distance[now_node] + next_edge
        pq.put((distance[next_node], next_node)) # put 할때 조심, 노드가 뒤

for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])