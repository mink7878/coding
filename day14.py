import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
q = PriorityQueue()

for _ in range(N):
  x = int(input())

  if x == 0:
    if q.empty():
      print(0)
    else:
      print(q.get()[1])

  else:
    q.put((abs(x), x)) # python에서는 [-1, 1, -2, 2] (절대값 > 음수 순)
  
