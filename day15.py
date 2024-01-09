# DFS  > 인접리스트 & 방문리스트 > 재귀

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # '재귀'할때 써주기  (python 1000으로 제한)

N, M = map(int, input().split())
A = [[] for _ in range(N+1)] # 인접리스트
visited = [False] * (N+1) # 방문리스트

# 그래프 정의 (인접리스트)
for _ in range(M):
  u, v = map(int, input().split())
  A[u].append(v)
  A[v].append(u)


def DFS(node):
  visited[node] = True
  for k in A[node]:
    if not visited[k]:
      DFS(k)
  
cnt = 0

for i in range(1, N+1):
  if not visited[i]:
    cnt += 1
    DFS(i)


print(cnt)