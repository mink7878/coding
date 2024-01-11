## DFS > 인접리스트, 방문리스트 > 재귀
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
stack = []
arrive = False

for _ in range(M):
  a, b = map(int, input().split())
  A[a].append(b)
  A[b].append(a)


def DFS(x, depth):
  global arrive
  if depth == 5:
    arrive = True
    return  # 함수 탈출 (break : for문 탈출)

  visited[x] = True
  for k in A[x]:
    if not visited[k]:
      DFS(k, depth + 1)
  visited[x] = False  # 탐색 실패한 경우 >>> 방문 취소!!


for i in range(N):
  DFS(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)
