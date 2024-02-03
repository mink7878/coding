## BOJ, 1948번: 임계경로
# 임계경로 >>> 전체 중에서 여러 경로가 동시에 이루어질 때, 가장 오래 걸리는 경로
# 위상정렬 >>> 진입차수 리스트 + 스택/큐

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 도시 수
M = int(input()) # 도로 수
A = [[] for _ in range(N+1)]
reversedA = [[] for _ in range(N+1)]
indegree = [0] * (N+1)


for _ in range(M):
  s, e, edge = map(int, input().split())
  A[s].append((e, edge))
  reversedA[e].append((s, edge))
  indegree[e] += 1

start, end = map(int, input().split())

q = deque()
q.append(start)

answer = [0] * (N+1)

# 정방향 진입차수 리스트 생성
while q:
  now = q.popleft()
  for next in A[now]:
    indegree[next[0]] -= 1
    answer[next[0]] = max(answer[next[0]], answer[now] + next[1]) # 각 도시의 임계 경로 리스트
    if indegree[next[0]] == 0:
      q.append(next[0])



q.clear() ## 모든 원소 지우기

cnt = 0
visited = [False] * (N+1)
q.append(end)
visited[end] = True

while q:
  now = q.popleft()
  for next in reversedA[now]:
    if answer[next[0]] + next[1] == answer[now]:
      cnt += 1
      if not visited[next[0]]: ######## 이미 방문한 노드는 없애 줘야 함!!! (위상정렬 특징)
        visited[next[0]] = True ########
        q.append(next[0])

print(answer[end])
print(cnt)