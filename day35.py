## union-find >>> 재귀, parent 리스트

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find(v):
  if v == parent[v]:
    return v

  else:
    parent[v] = find(parent[v])
    return parent[v]
  
def union(a, b):
  pa = find(a)
  pb = find(b)
  parent[pa] = pb

A = []
for i in range(N):
  tmp = list(map(int, input().split()))
  A.append(tmp)
  for j in range(N):
    if A[i][j] == 1:
      union(i+1, j+1)

plan = list(set(list(map(int, input().split()))))
idx = find(plan[0])
IsConnect = True
for i in plan:
  if find(i) != idx:
    IsConnect = False
    break

if IsConnect:
  print("YES")
else:
  print("NO")