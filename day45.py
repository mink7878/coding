## 모든 노드 쌍에 관해 경로가 있는지 여부를 확인하는 방법 >>> 플로이드-워셜
## 어딘가를 거쳐서 도착한다

import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
  tmp = list(map(int, input().split()))
  graph.append(tmp)

for k in range(N):
  for s in range(N):
    for e in range(N):
      if graph[s][k] == 1 and graph[k][e] == 1:
        graph[s][e] = 1

for ans in graph:
  print(*ans)