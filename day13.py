from collections import deque

N = int(input())
q = deque()

for i in range(1, N+1):
  q.append(i)

while len(q) != 1:
  top = q.popleft()
  top_nxt = q.popleft()
  q.append(top_nxt)

print(q[0])