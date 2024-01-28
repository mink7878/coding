## union-find >>> 재귀, parent 리스트

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)] # 나 자신으로 초기화

# find : 각 집합의 "최종 대표"가 나올 때까지 계속 찾기
# 최종 대표? = 자기 자신이 대표, 초기화 후 바뀐적 x
def find(v):
  if v == parent[v]:
    return v

  else:
    parent[v] = find(parent[v]) # 최종 대표 찾아서 넣어주기 (재귀)
    return parent[v]
  

# union : 같은 집합으로 만들기
def union(a, b):
  pa = find(a)
  pb = find(b)
  parent[pa] = pb
  

for _ in range(M):
  q, a, b = map(int, input().split())

  if q == 0: # union
    union(a, b)

  else: # find
    if find(a) == find(b):
      print("YES")
    else:
      print("NO")