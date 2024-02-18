## 벨만-포드 >>> 음수 가중치 허용
## 그래프 구현 >>> 에지 리스트

import sys
INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
distance = [INF] * (N+1)

for _ in range(M):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

# 초기화
distance[1] = 0

for _ in range(N-1): # 모든 edge 탐색 (업데이트 반복 횟수 N-1)
  for s, e, t in edges:
    if distance[s] != INF and distance[e] > distance[s] + t:
      distance[e] = distance[s] + t

###### 음수 사이클 존재 확인 ######
Cyc = False

for s, e, t in edges:
  if distance[s] != INF and distance[e] > distance[s] + t:
    Cyc = True

if not Cyc:
  for i in range(2, N+1):
    if distance[i] != INF:
      print(distance[i])
    else:
      print(-1)

else:
  print(-1)