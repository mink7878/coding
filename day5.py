# today : 오늘 날짜
# terms : 약관의 유효기간 =  [약관종류(A~Z), 유효기간(1~100m)]
# privacies : 수집된 개인정보 = [날짜, 약관종류]
# 모든 달은 28일까지 존재

def convert_day(t):
    year, month, day = map(int, t.split('.'))
    return year*12*28 + month*28 + day
    

def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    
    for term in terms:
        a, b = term.split()
        term_dict[a] = int(b) * 28
    
    for num, privacy in enumerate(privacies):
        st, term_type = privacy.split()
        if convert_day(st) + term_dict[term_type] <= convert_day(today):
            answer.append(num+1)

    return answer