# coding

### 유니온 파인드
- 분리집합 자료구조 / parent 리스트 / 재귀 (sys.setrecursionlimit(10000))
  - Union : 같은 집합으로 만들어주기
  - Find : 각 집합의 '최종대표'가 나올 때까지 계속 찾기 / 최종대표 = 자기 자신이 대표, 초기화한 후 바뀐 적 x

### 위상 정렬
- 사이클 x / 선후관계 / 정답 여러개 / 진입차수(indegree)
- 그래프 표현 : 가리키는 애 기준으로 표현
- 진입차수(indegree) : 니를 가리키는 에지 수
  - 임계 경로 : 전체 중에서 여러 경로가 동시에 이루어질 때, 가장 오래 걸리는 경로 / 에지 뒤집기 (reversedA) / 방문 리스트

### 다익스트라
- 양수 간선 / 최소 거리 / 우선순위 큐 / 방문 리스트 / 거리 리스트 / INF = int(1e9)
- 우선순위 큐 : 현재 연결된 노드 중 가장 적은 비용을 지니고 있는 노드를 빠르고 간편하게 찾을 수 있음
