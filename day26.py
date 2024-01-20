## 그리디 > 우선순위 큐 (PriorityQueue / heapq)
import sys
from queue import PriorityQueue

input = sys.stdin.readline
q = PriorityQueue()

N = int(input())
for _ in range(N):
  q.put(int(input()))

answer = 0
while q.qsize()> 1:
  x = q.get()
  y = q.get()

  tmp = x + y
  answer += tmp
  q.put(tmp)

print(answer)