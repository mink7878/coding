import collections

def solution(v):
    answer = []

    for i in zip(*v):
        val = collections.Counter(i)
        answer.append(val.most_common()[-1][0])

    return answer
