def dfs(i, j, kind, d):
    global start, result
    di = [1, 1, -1, -1]  # 북서 -> 북동 -> 남동 -> 남서
    dj = [-1, 1, 1, -1]

    if d > 3:
        return

    # 출발지로 돌아왔을 때 사각형이 완성되었는지 확인
    if d == 3 and i == start[0] and j == start[1]:
        result = max(result, len(kind))
        return

    for num in range(d, d + 2):  # 현재 방향 유지 or 한 번 회전 가능
        if num >= 4:  # 방향이 3(남서)까지여야 함
            continue
        ni, nj = i + di[num], j + dj[num]

        # 이동할 곳이 유효한 범위 내에 있고, 같은 디저트를 먹지 않았다면 탐색 진행
        if 0 <= ni < N and 0 <= nj < N and dessert[ni][nj] not in kind:
            dfs(ni, nj, kind + [dessert[ni][nj]], num)  # 리스트 복사로 공유 방지


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # N*N 사각형
    dessert = [list(map(int, input().split())) for _ in range(N)]

    result = -1

    for row in range(N - 2):  # 최소 4개 카페를 들러야 하므로 위쪽 2줄은 탐색 불필요
        for col in range(1, N - 1):  # 가장자리는 탐색할 필요 없음
            start = (row, col)
            dfs(row, col, [dessert[row][col]], 0)  # 시작점 설정

    print(f"#{test_case} {result}")
