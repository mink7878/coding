from collections import deque

def solution(land):
    n = len(land) # 세로
    m = len(land[0]) # 가로
    
    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[False]*m for _ in range(n)]
    checked = [0 for _ in range(m)]
    
    def BFS(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True
    
        min_y, max_y = j, j
        cnt = 0
        
        while q: # 빈 큐 될때까지
            now = q.popleft()
            min_y = min(min_y, now[1])
            max_y = max(max_y, now[1])
            cnt += 1
            
            for k in range(4): # 상하좌우 확인
                cx = now[0] + dx[k]
                cy = now[1] + dy[k]
                if 0 <= cx < n and 0 <= cy < m: # 좌표유효성 확인
                    if not visited[cx][cy] and land[cx][cy]: # 방문여부 & 까만색 확인
                        visited[cx][cy] = True
                        q.append((cx, cy))
        
        for c in range(min_y, max_y+1):
            checked[c] += cnt
            
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]: # 방문여부 & 까만색 확인
                BFS(i, j)

    return max(checked)