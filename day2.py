def solution(board, h, w):
    cnt = 0
    
    # 오른(0) / 아래(1) / 위(2) / 왼(3)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # 1. 전체 다 돌면서 찾기
    # 2. 주어진 좌표 기준으로 주변만 찾기 >>> 선택
    
    target = board[h][w]
    
    for i in range(4):
        ch = h + dh[i]
        cw = w + dw[i]
        
        if (0 <= ch < len(board) and 0 <= cw < len(board)) and (board[ch][cw] == target):
            cnt += 1
    
    return cnt