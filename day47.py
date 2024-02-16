## MST (최소신장트리)
## Spanning Tree : 신장트리 : 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.
### 대표적인 MST >>> 크루스칼 알고리즘
### 그래프 표현 >>> 에지 리스트

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 노드개수 & 에지(union 연산)개수 입력 받기
N, M = map(int, input().split())
parent = [0] * (N+1)

# 나 자신을 부모로 초기화
for i in range(N+1):
  parent[i] = i

def find(v):
  if v == parent[v]:
    return v
  else:
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

edges = []
result = 0

for _ in range(M):
  s, e, cost = map(int, input().split())
  edges.append((cost, s, e))

edges.sort() # cost 적은게 젤 앞 (PriorityQueue 사용 가능)

for edge in edges:
  cost, s, e = edge
  # 두 노드의 부모가 다르면 = 연결해도 사이클이 생기지 않는다면
  if find(s) != find(e):
    union(s, e)
    result += cost

print(result)