
# 남은 벽돌 개수 확인 함수 ( 벽돌 배열 , 가로 , 세로 매개변수 받음)
def brick(arr, w, h):
    bricks = 0
    for i in range(w):
        for j in range(h):
            if arr[i][j]:
                bricks += 1
    return bricks

# dfs로 구슬 쏘기 구현
# 행,열 인덱스 , space(구슬 폭발 범위) 매개변수 받음
def dfs(i,j,s):
    bomb = s[i][j] - 1
    s[i][j] = 0
    if bomb > 1:
        for delta in range(4):
            for k in range(bomb):
                ni = i + di[delta] * k+1
                nj = j + dj[delta] * k+1
                if s[ni][nj] == 1:
                    s[ni][nj] = 0
                elif s[ni][nj] > 1:
                    dfs(ni,nj,s)
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, W, H = map(int,input().split())              # N은 구슬 쏘는 횟수 / W 가로 길이 / H 세로 길이

    space = [list(map(int, input())) for _ in range(H)]

    fix_j = 0                                           # 열 인덱스

    min_bricks = 99999                                  # 남은 벽돌 개수 (최대한 많이 깨기)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while fix_j < W:                                    # 모든 열 구슬 쏴보기
        copy_space = space
        for cnt in range(N):                            # 구슬은 N번 쏠 수 있음.
            if cnt == 0:                                 # cnt = 0 일때는 j 가 고정
                for row in range(H):
                    if copy_space[row][fix_j]:
                        dfs(row,fix_j,copy_space)
                        break
            else:
                for col in range(W):
                    copy_copy_space = copy_space
                    for row in range(H):
                        if copy_copy_space[row][col]:
                            dfs(row,col,copy_copy_space)
                    result = brick(copy_copy_space, W, H)  # 쏠때마다 남은 벽돌 수 확인
                    if result < min_bricks:
                        min_bricks = result

        fix_j += 1


    print(f"{test_case} {min_bricks}")
    # ///////////////////////////////////////////////////////////////////////////////////
