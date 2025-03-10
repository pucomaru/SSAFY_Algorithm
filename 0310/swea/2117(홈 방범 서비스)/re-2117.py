from collections import deque

def bfs(si, sj):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    visited[si][sj] = 1
    q.append([si, sj])

    while q:
        xi, xj = q.popleft()

        for d in range(4):
            ni = xi + dx[d]
            nj = xj + dy[d]

            if 0 <= ni < N and 0 <= nj < N:
                visited[ni][nj] = visited[xi][xj] + 1
                q.append([ni, nj])
    return visited

def profit(arr, k):
    global max_profit

    # 운영 비용
    cost = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] <= k:
                cost += 1

    # 서비스 제공받는 집 수
    provide = 0
    for hi, hj in home:
        if arr[hi][hj] <= k:
            provide += 1

    total_profit = (provide * M) - cost

    if total_profit > max_profit:
        max_profit = total_profit

    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())         # N 도시의 크기 / M 하나의 집이 지불할 수 있는 비용

    city = [list(map(int, input().split())) for _ in range(N)]

    max_profit = -9999999

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 집 인덱스들
    home = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                home.append([i, j])

    # 최대 이익 구해보기
    for i in range(N):
        for j in range(N):
            range_map = bfs(i, j)

            for k in range(1, N):
                profit(range_map, k)

    print(f"{test_case} {max_profit}")


    # ///////////////////////////////////////////////////////////////////////////////////
