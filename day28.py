## 4 type으로 구분해서 저장
# 양수 / 음수 / 1 / 0
from queue import PriorityQueue
import sys

input = sys.stdin.readline

N = int(input())

plusq = PriorityQueue()
minusq = PriorityQueue()
zero = 0
one = 0

for _ in range(N):
  tmp = int(input())

  if tmp > 1:
    plusq.put(tmp * -1)  # 양수 내림차순 정렬!

  elif tmp < 0:
    minusq.put(tmp)  # 음수는 -3, -1 (절댓값) 순서로 나옴

  elif tmp == 1:
    one += 1

  elif tmp == 0:
    zero += 1

sum = 0

while plusq.qsize() > 1:
  first = plusq.get() * -1
  second = plusq.get() * -1
  sum += first * second

if plusq.qsize() > 0:
  sum += plusq.get() * -1

while minusq.qsize() > 1:
  first = minusq.get()
  second = minusq.get()
  sum += first * second

if minusq.qsize() > 0:
  if zero == 0:
    sum += minusq.get()

sum += one
print(sum)
