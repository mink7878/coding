## 완탐 + BFS
# 6가지 경우의 수

import sys
from collections import deque
input = sys.stdin.readline

def pour(x, y):
  if not visited[x][y]:
    visited[x][y] = True
    q.append((x, y))


def BFS():
  while q:
    x, y = q.popleft()
    z = C - x - y

    if x == 0:
      answer.append(z)

    # x >>> y
    water = min(x, B - y) # 옮길 수 있는 물의 양
    pour(x - water, y + water)

    # x >>> z
    water = min(x, C - z)
    pour(x - water, y)

    # y >>> x
    water = min(y, A - x)
    pour(x + water, y - water)

    # y >>> z
    water = min(y, C - z)
    pour(x, y - water)

    # z >>> x
    water = min(z, A - x)
    pour(x + water, y)

    # z >>> y
    water = min(z, B - y)
    pour(x, y + water)



A, B, C = map(int, input().split())

q = deque()
q.append((0,0)) # A, B가 빈 상태에서 시작

visited = [[False] * (B+1) for _ in range(A+1)]
visited[0][0] = True # 초기화 (처음 위치)

answer = []

BFS()

answer.sort()

for i in answer:
  print(i, end=' ')