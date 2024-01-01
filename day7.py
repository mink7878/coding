# 양 끝에서 시작 후 좁혀가기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

cnt = 0

sp = 0
ep = n-1

while sp < ep:
  if ingredients[sp] + ingredients[ep] == m:
    cnt += 1
    # 고유한 번호 사용해야 하니까 둘 다 이동
    sp += 1
    ep -= 1

  elif ingredients[sp] + ingredients[ep] > m:
    ep -= 1

  else:
    sp += 1

print(cnt)