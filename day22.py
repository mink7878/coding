## 최대 하나 강의 길이 = 크기 '9' >>> 블루레이 6개
## 전체 강의 길이 합 = 1+...+9 = 크기 '45' >>> 블루레이 1개

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = 0

for i in lessons:
  end += i

while start <= end:
  midi = int((start+end)/2)
  
  checkSum = 0
  cnt = 0
  for k in lessons:
    if checkSum + k > midi:
      cnt += 1
      checkSum = 0
    checkSum += k

  if checkSum != 0:
    cnt += 1

  if cnt > M: # 필요한 블루레이 너무 많음 >>> 하나의 크기 늘려주기
    start = midi + 1

  else: # 필요한 블루레이 너무 적거나 같음 >>> 하나의 크기 줄여주기
    end = midi - 1
    
  
print(start)