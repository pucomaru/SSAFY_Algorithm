
#import sys
#sys.stdin = open("input.txt", "r")

# dfs를 이용해 모든 방 가는 경로 탐색하고 가장 많은 개수의 방을 이동한 처음 인덱스 를 결과로 출력
# 이동할 수 있는 방의 개수가 최대인 방 여럿이라면 적힌 수가 가장 적은 것을 출력

# 행 / 열 / 시작인덱스 / 이동 횟수
def dfs(r, c, s, move):
    global max_move
    global min_start_room

    m = 0
    # 이동 조건 = 가는 곳에 방이 있는 경우 + 지금 있는 방번호보다 1
    for d in range(4):
        ni = r + di[d]
        nj = c + dj[d]
        if 0 <= ni < N and 0 <= nj < N and room[ni][nj] - room[r][c] == 1:
            dfs(ni, nj, s, move+1)
            m += 1

    # 이동 할 수 없을 때 비교 m==0 이라는 뜻은 델타를 한번도 안돌았다는 뜻 . 그럼 지금 인덱스에서 이동을 못한 상태
    if m == 0:
        # 이동횟수가 저장된 횟수보다 크면 갱신
        if move > max_move:
            max_move = move
            min_start_room = room[s[0]][s[1]]

        # 이동횟수가 저장된 횟수랑 같으면 방번호가 더 작은걸 저장해줌
        elif move == max_move and room[s[0]][s[1]] < min_start_room:
            min_start_room = room[s[0]][s[1]]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_move = -1
    min_start_room = 1e9

    di = [0, 1, 0, -1]   # 우 / 하 / 좌 / 상
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            start_idx = (i, j)
            dfs(i, j, start_idx, 1)

    print(f"#{test_case} {min_start_room} {max_move}")
    # ///////////////////////////////////////////////////////////////////////////////////
