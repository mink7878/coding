import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N

for i in range(N):
  A[i] = int(input())

stack = []
num = 1
result = True
answer = ''

for j in range(N):
  curr = A[j]
  ## append
  if curr >= num:
    while curr >= num:
      stack.append(num)
      num += 1
      answer += '+\n'
    stack.pop()
    answer += '-\n'
  ## pop
  else:
    n = stack.pop()
    if n > curr:
      print('NO')
      result = False
      break
    else:
      answer += '-\n'

if result:
  print(answer)