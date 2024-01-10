import math
import sys
sys.setrecursionlimit(10000)
N = int(input())


def isPrime(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

def DFS(y):
  if len(str(y)) == N:
    print(y)
  
  for k in range(1, 10):
    if k % 2 == 0:
      continue
    else:
      if isPrime(y*10 + k):
        DFS(y*10 + k)


DFS(2)
DFS(3)
DFS(5)
DFS(7)