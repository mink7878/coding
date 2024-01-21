A = list(map(str, input().split('-')))

def mySum(str):
  B = str.split('+')

  lst_sum = 0
  for i in B:
    lst_sum += int(i)
    
  return lst_sum

answer = 0
for j in range(len(A)):
  tmp = mySum(A[j])
  if j == 0:
    answer += tmp

  else:
    answer -= tmp

print(answer)