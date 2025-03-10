
# 영역찾기 함수
def dfs(r, c, k, cnt, v):
    global visited
    global home_cnt
    v[r][c] = 1

    if cnt < k:
        for d in range(4):
            ni = r + di[d]
            nj = c + dj[d]

            if 0 <= ni < N and 0 <= nj < N:
                v[ni][nj] = 1
                dfs(ni, nj, k, cnt+1, v)
    return v

def profit(arr):
    global max_profit
    # 서비스 구역 운영 비용
    cost = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                cost += 1
    # 서비스 제공받는 집들
    provide = 0
    for hi, hj in house:
        if arr[hi][hj] == 1:
            provide += 1

    profits = (M * provide) - cost

    if max_profit < profits:
        max_profit = profits
        home_cnt = provide

    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())                    # N 도시 크기 / M 하나의 집이 지불할 수 있는 비용

    city = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    visited = [[0] * N for _ in range(N)]

    # 집 위치 인덱스 담을 리스트
    house = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append([i, j])

    # 최대 이익을 담을 변수
    max_profit = -99999
    home_cnt = 0

    # 집 위치 한 곳에서 보안회사 이익을 구해봄
    for i in range(len(house)):
        for K in range(1, N):
            visited = [[0] * N for _ in range(N)]
            check = dfs(house[i][0], house[i][1], K, 1, visited)
            profit(check)

    print(f"#{test_case} {home_cnt}")


    # ///////////////////////////////////////////////////////////////////////////////////
