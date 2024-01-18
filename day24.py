import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # 동전 종류 # 가치 합
A = []
answer = 0

for _ in range(N):
  A.append(int(input()))

for i in range(N - 1, -1, -1):  # 역순 >>> sort, 갱신 x
  if A[i] <= K:
    answer += int(K / A[i])
    K %= A[i]

print(answer)