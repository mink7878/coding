## 트리 지름
## 1. 임의의 점 x에서 가장 먼 점 y 찾음
## 2. y에서 가장 먼 점 z 찾음
## 3. 트리 지름 = y 〜 z
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
  lst = list(map(int, input().split()))
  idx = 0
  S = lst[idx]
  idx += 1
  
  while True:
    E = lst[idx]
    if E == -1:
      break
    V = lst[idx+1]
    A[S].append((E, V))
    idx += 2

visited = [False] * (N+1)
distance =  [0] * (N+1)

def BFS(x):
  q = deque()
  q.append(x)
  visited[x] = True
  while q:
    now = q.popleft()
    for k in A[now]:
      if not visited[k[0]]:
        visited[k[0]] = True
        q.append((k[0]))
        distance[k[0]] = distance[now] + k[1]


BFS(1)
Max = 1

for i in range(2, N+1):
 if distance[Max] < distance[i]:
   Max = i

visited = [False] * (N+1)
distance =  [0] * (N+1)
BFS(Max)
distance.sort()
print(distance[-1])