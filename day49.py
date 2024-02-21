## MST 최소신장트리 >>> 최소 연결 부분트리 & 사이클 x
### edge list 그래프 구현 >>> 우선순위 큐
### union-find >>> 재귀
### N-1 edge

import sys
from queue import PriorityQueue
sys.setrecursionlimit(100000)
input = sys.stdin.readline

V, E = map(int, input().split())
parent = [0] * (V+1)

for i in range(V+1):
  parent[i] = i

pq = PriorityQueue()

for _ in range(E):
  A, B, C = map(int, input().split())
  pq.put((C, A, B))

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

edges = 0
answer = 0

while edges < V-1: # MST 항상 V-1 사용
  c, a, b = pq.get()
  if find(a) != find(b):
    union(a, b)
    answer += c
    edges += 1

print(answer)