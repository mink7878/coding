## 이진탐색 > 정렬! > 절반씩 줄이다가 중앙값과 같아지면 stop

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
find_num = list(map(int, input().split()))

A.sort() # 이진탐색 >>> 정렬부터

for i in range(M):
  find = False
  target = find_num[i]

  ## 인덱스 이용
  start = 0
  end = len(A)-1

  while start <= end:
    median_idx = int((start+end)/2) # 중앙값 인덱스
    median_num = A[median_idx] # 중앙값 실제값
    if target < median_num:
      end = median_idx - 1
    elif target > median_num:
      start = median_idx + 1
    else:
      find = True
      break

  if find:
    print(1)
  else:
    print(0)

