# dfs로 대각선 갈 수 있는 방향 계속 계속 계속 가고 첫 시작 인덱스랑 이동 후 인덱스 같으면 리턴

# 현재 행, 열 , 시작 인덱스, 이동횟수 , 디저트종류(리스트) 매개변수로 받음
def dfs(row,column, start, move, kind, now_direction ):
    global result
    print(kind)
    # 제일 작은 사각형을 만들라면 최소 3번은 움직여야함. 그리고 시작 인덱스와 이동 인덱스가 같아야지 조건 충족
    if move > 3 and row == start[0] and column == start[1]:
        if len(kind) > result:
            result = len(kind)
            print(len(kind))
        return

    dy = [-1, -1, 1, 1]             # 북서 / 북동 / 남서 / 남동 방향
    dx = [-1, 1, -1, 1]

    # 북서 방향은 0 / 북동 방향은 1 / 남동 방향은 2 / 남서 방향은 3 / 처음은 0
    for idx in range(4):
        if 0 <= row + dy[idx] < N and 0 <= column + dx[idx] < N:        # 이동 방향이 인덱스 범위를 벗어나면 안됨
            ## 북서 ↖ 방향으로 갈 때 (전 방향이 북서 0, 처음 -1, 남서 3 일때만 갈 수 있음)
            if (idx == 0 and (dessert[row + dy[idx]][column + dx[idx]] not in kind) and
                    (now_direction == -1 or now_direction == 0 or now_direction == 3 )):
                kind.append(dessert[row + dy[idx]][column + dx[idx]])
                dfs(row + dy[idx], column + dx[idx], start, move+1, kind, 0)
                kind.pop()

            ## 북동↗ 방향으로 갈 때 (전 방향이 북동 1, 북서 0, 처음 -1 일때만 갈 수 있음)
            if (idx == 1 and (dessert[row + dy[idx]][column + dx[idx]] not in kind) and
                    (now_direction == -1 or now_direction == 1 or now_direction == 0 )):
                kind.append(dessert[row + dy[idx]][column + dx[idx]])
                dfs(row + dy[idx], column + dx[idx], start, move+1, kind, 1)
                kind.pop()

                ## 남동↘ 방향으로 갈 때 (전 방향이 남동 2, 북동 1, 처음 -1 일때만 갈 수 있음)
            if (idx == 2 and (dessert[row + dy[idx]][column + dx[idx]] not in kind) and
                    (now_direction == -1 or now_direction == 1 or now_direction == 2)):
                kind.append(dessert[row + dy[idx]][column + dx[idx]])
                dfs(row + dy[idx], column + dx[idx], start, move+1, kind, 2)
                kind.pop()

            ## 남서↙ 방향으로 갈 때 (전 방향이 남서 3, 남동 2, 처음 -1 일때만 갈 수 있음)
            if (idx == 3 and (dessert[row + dy[idx]][column + dx[idx]] not in kind) and
                    (now_direction == -1 or now_direction == 2 or now_direction == 3 )):
                kind.append(dessert[row + dy[idx]][column + dx[idx]])
                dfs(row + dy[idx], column + dx[idx], start, move+1, kind, 3)
                kind.pop()
        else:
            pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())            # N * N 정사각형
    dessert= [list(map(int,input().split())) for _ in range(N)]

    result = -1

    for i in range(N):
        for j in range(N):
            start_idx = (i,j)
            move_cnt = 0                # 이동 횟수 dfs 종료 조건을 위해 만든 변수
            dessert_kind = []           # 디저트 종류 리스트
            dessert_kind.append(dessert[i][j])
            direction = -1               # 움직인 방향 ( 북동 방향으로 움직였으면 또 북동방향 쪽으로 가거나 남동 방향으로 가야함)
            dfs(i,j,start_idx , move_cnt, dessert_kind, direction)

    print(f"{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
