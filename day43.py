import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra():
  pq = []
  heapq.heappush(pq, (graph[0][0], 0, 0))
  distance[0][0] = 0

  while pq:
    c, x, y = heapq.heappop(pq)

    if x == N-1 and y == N-1:
      print(f'Problem {cnt}: {distance[x][y]}')
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        nc = c + graph[nx][ny]
        if nc < distance[nx][ny]:
          distance[nx][ny] = nc
          heapq.heappush(pq, (nc, nx, ny))

cnt = 1

while True:
  N = int(input())
  if N == 0:
    break

  graph = [list(map(int, input().split())) for _ in range(N)]
  distance = [[INF]*(N+1) for _ in range(N)]

  dijkstra()
  cnt += 1