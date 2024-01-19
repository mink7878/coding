import sys
input = sys.stdin.readline

N = int(input())
A = [[0]*2 for _ in range(N)]

for i in range(N):
  s, e = map(int, input().split())
  A[i][0] = s
  A[i][1] = e

A.sort(key = lambda x:(x[1], x[0])) # 이중 for문 정렬

tmpa = 0
tmpb = 0
cnt = 0
for a, b in A:
  if tmpb <= a:
    tmpa = a
    tmpb = b
    cnt += 1

print(cnt)
    