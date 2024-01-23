## 소수 판별 (에라토스테네스의 체) >>> 주어진 범위 전부 돌기, 제곱근까지만 확인 (짝꿍)
import math
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
A = [0] * (N + 1)

for i in range(2, N + 1):
  A[i] = i

for i in range(2, int(math.sqrt(N)) + 1):
  if i == 0:
    continue
  for j in range(i + i, N + 1, i):  ## 첫수의 배수 확인
    A[j] = 0

for i in range(M, N + 1):
  if A[i] != 0:
    print(A[i])
