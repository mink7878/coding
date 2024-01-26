## BFS > DFS? : BFS는 해당 깊이에서 갈 수 있는 노드 탐색을 마친 후 다음 깊이로 넘어갈 때 적합
## 깊이가 중요한 문제니까 DFS

## 이분 그래프 판별? '사이클'

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

K = int(input())
IsBG = True # 이분그래프 판별용


def DFS(v):
  global IsBG
  visited[v] = True
  for i in A[v]:
    if not visited[i]: # 방문 안 했다면
      check[i] = (check[v]+1)%2
      DFS(i)
    elif check[i] == check[v]: # 방문 했었는데, 같은 그룹에 속하는 경우
      IsBG = False


for _ in range(K):
  V, E = map(int, input().split())
  A = [[] for _ in range(V+1)]

  visited = [False] * (V+1)
  check = [0] * (V+1)
  IsBG = True
  for _ in range(E):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

  for i in range(1, V+1):
    if IsBG:
      DFS(i)
    else:
      break

  if IsBG:
    print('YES')
  else:
    print('NO')