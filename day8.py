import sys
input = sys.stdin.readline


def myadd(c):
  global myList, checkList, checkSecret
  if c == 'A':
    myList[0] += 1
    if myList[0] == checkList[0]:
      checkSecret += 1

  elif c == 'C':
    myList[1] += 1
    if myList[1] == checkList[1]:
      checkSecret += 1
      
  elif c == 'G':
    myList[2] += 1
    if myList[2] == checkList[2]:
      checkSecret += 1

  elif c == 'T':
    myList[3] += 1
    if myList[3] == checkList[3]:
      checkSecret += 1

def myremove(c):
  global myList, checkList, checkSecret
  if c == 'A':
    if myList[0] == checkList[0]:
      checkSecret -= 1
    myList[0] -= 1

  elif c == 'C':
    if myList[1] == checkList[1]:
      checkSecret -= 1
    myList[1] -= 1

  elif c == 'G':
    if myList[2] == checkList[2]:
      checkSecret -= 1
    myList[2] -= 1
  
  elif c == 'T':
    if myList[3] == checkList[3]:
      checkSecret -= 1
    myList[3] -= 1

S, P = map(int, input().split())
A = list(input())

# 기준 리스트
checkList = list(map(int, input().split())) # {‘A’, ‘C’, ‘G’, ‘T’}
# 현재 리스트
myList = [0]*4
# 4개 문자열 모두 만족했는지 체크 (4되면 만족)
checkSecret = 0

answer = 0

# 기준 리스트 확인 (미리 0있는지 체크)
for i in checkList:
  if i == 0:
    checkSecret += 1

# 처음 0~P-1 확인
for i in range(P):
  myadd(A[i])

if checkSecret == 4:
  answer += 1

for i in range(P, S):
  j = i-P
  myadd(A[i])
  myremove(A[j])
  if checkSecret == 4:
    answer += 1

print(answer)