# 1 = 빵
# 2 = 야채
# 3 = 고기
# 포장 순서 : 빵-야채-고기-빵 = [1, 2, 3, 1]

def solution(ingredient):
    answer = 0
    stack = []
    
    for ing in ingredient:
        stack.append(ing)
        
        # 뒤에서 부터 확인하기
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            for _ in range(4):
                stack.pop()
    
    return answer