## 다익스트라 >>> 양수 간선 / 최소 거리 / 우선순위 큐

import sys
from queue import PriorityQueue
INF = int(1e9)
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수
A = [[] for _ in range(N+1)]

for _ in range(M):
  s, e, v = map(int, input().split())
  A[s].append((e, v))

S, E = map(int, input().split())

distance = [INF] * (N+1)
visited = [False] * (N+1)

pq = PriorityQueue()
pq.put((0, S))
distance[S] = 0

while pq.qsize() > 0:
  now = pq.get()
  now_node = now[1]

  if visited[now_node]:
    continue
  visited[now_node] = True
  for next in A[now_node]:
    next_node = next[0]
    next_v = next[1]
    if not visited[next_node]:
      if distance[next_node] > distance[now_node] + next_v:
        distance[next_node] = distance[now_node] + next_v
        pq.put((distance[next_node], next_node))

print(distance[E])