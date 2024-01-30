import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
known_people = list(map(int, input().split()))[1:]
party = []
parent = list(range(N+1))
answer = 0

def find(v):
  if v == parent[v]:
    return v

  else:
    parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
  pa = find(a)
  pb = find(b)
  parent[pa] = pb


answer = 0
for _ in range(M):
  party_info = list(map(int, input().split()))
  party_n = party_info[0]
  party_lst = party_info[1:]
  for j in range(party_n-1):
    union(party_lst[j], party_lst[j+1])
  party.append(party_lst)


answer = 0
for i in range(M):
  iP = True
  firstP = party[i][0]
  for j in range(len(known_people)):
    if find(firstP) == find(known_people[j]):
      iP = False
      break

  if iP:
    answer += 1

print(answer)