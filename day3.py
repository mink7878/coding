# ext : 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
# val_ext : 뽑아낼 정보의 기준값을 나타내는 정수
# sort_by : 정보를 정렬할 기준이 되는 문자열 (오름차순)

def solution(data, ext, val_ext, sort_by):
    answer = []
    lst = ["code", "date", "maximum", "remain"]
    
    for i in range(len(data)):
        if data[i][lst.index(ext)] < val_ext:
            answer.append(data[i])

    answer.sort(key=lambda x:x[lst.index(sort_by)])
    
    return answer