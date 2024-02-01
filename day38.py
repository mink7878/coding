## 위상정렬 >>> indegree 리스트 & 큐/스택
# 사이클 x, 순서

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 건물의 종류 수
A = [[] for _ in range(N+1)] # 그래프
building_time = [0] * (N+1) # 건물 짓는 데 걸리는 시간
indegree = [0] * (N+1) # 진입 차수 리스트
result = [0] * (N+1) # 결과

for i in range(1, N+1):
  tmp = list(map(int, input().split()))
  building_time[i] = tmp[0]
  del tmp[0]

  # 찌르는 애 기준으로 그래프
  idx = 0
  while True:
    node = tmp[idx]
    idx += 1
    if node == -1:
      break

    A[node].append(i)
    indegree[i] += 1


q = deque()

for i in range(1, N+1):
  if indegree[i] == 0:
    q.append(i)
    result[i] = building_time[i]


while q:
  now = q.popleft()
  for next in A[now]:
    indegree[next] -= 1
    result[next] = max(result[next], result[now] + building_time[next]) ### 이 부분 추가 (중요)
    if indegree[next] == 0:
      q.append(next)

for i in range(1, N+1):
  print(result[i])