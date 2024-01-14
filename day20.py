## BFS > queue
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []

# for _ in range(N):
#   A.append(list(map(int, input()))) ## stdin 사용 xx

for _ in range(N):
  A.append(list(map(int, input().rstrip())))  ## stdin 사용시 rstrip


def BFS(x, y):
  ## 동남서북
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  q = deque()
  q.append((x, y))

  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if A[nx][ny] == 1:
          q.append((nx, ny))
          A[nx][ny] = A[cx][cy] + 1
  return A[N - 1][M - 1]

print(BFS(0, 0))