import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

mydeque = deque()

for i in range(N):
  # 지금 가장 큰 값 vs. 새로 들어온 값
  # 지금 값이 크면 제거
  while mydeque and mydeque[-1][1] > A[i]:
    mydeque.pop()

  mydeque.append((i, A[i]))

  if mydeque[0][0] <= i - L:  # 나 ~ L구간 아닌 앞 범위 제거
    mydeque.popleft()

  print(mydeque[0][1], end=' ')
