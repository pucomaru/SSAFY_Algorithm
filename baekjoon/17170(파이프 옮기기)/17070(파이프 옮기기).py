# 새 집의 크기 N * N
# 각각의 칸은 (r, c) 행 / 열 
# 각각의 칸은 빈 칸이거나 벽이다.
# 파이프 방향 -> , 대각선아래 , 아래
# 파이프 미는 방향 오른쪽, 아래 , 오른쪽 아래 대각선 방향
# 파이프가 가로로 놓여진 경우에 가능한 이동 방법 2가지 : 가로 ,오른쪽아래 대각선
# 파이프가 세로로 놓여진 경우에 가능한 이동 방법 2가지 : 세로 , 오른쪽아래 대각선
# 파이프가 오른쪽아래 대각선으로 놓여진 경우에 가능한 이동 방법 3가지 : 가로, 세로 ,오른쪽 아래 대각선
# 파이프는 2개의 연속된 칸을 차지하는 크기

# 처음 파이프는 (1,1), (1,2) 위치 (방향은 가로)

def dfs(end, dir):
    global result
    global home

    r,c = end

    if r == N-1 and c == N-1:
        result += 1
        return

    # 방향이 가로 일경우에는 가로, 대각선만 이동 가능
    if dir == direction[0]:
        for d in [0, 2]:
            nr = r + dr[d]
            nc = c + dc[d]

            if d == 2:
                if 1 <= nr < N and 1 <= nc < N and home[nr][nc] != 1 and home[nr-1][nc] != 1 and home[nr][nc-1] != 1:
                    dfs([nr, nc], d)

            elif 0 <= nr < N and 0 <= nc < N and home[nr][nc] != 1:
                dfs([nr, nc], d)

    # 방향이 세로일 경우에는 세로, 대각선만 이동 가능
    elif dir == direction[1]:
        for d in [1, 2]:
            nr = r + dr[d]
            nc = c + dc[d]

            if d == 2:
                if 1 <= nr < N and 1 <= nc < N and home[nr][nc] != 1 and home[nr-1][nc] != 1 and home[nr][nc-1] != 1:
                    dfs([nr, nc], d)

            elif 0 <= nr < N and 0 <= nc < N and home[nr][nc] != 1:
                dfs([nr, nc], d)

    # 방향이 대각선일 경우에는 가로, 세로 ,대각선 가능
    elif dir == direction[2]:
        for d in [0, 1, 2]:
            nr = r + dr[d]
            nc = c + dc[d]
            if 1 <= nr < N and 1 <= nc < N and home[nr][nc] != 1 and home[nr-1][nc] != 1 and home[nr][nc-1] != 1:
                dfs([nr, nc], d)

# N : 집의 크기
N = int(input())

# 집의 상태 ( 빈칸은 0 , 벽은 1)
home = [list(map(int, input().split())) for _ in range(N)]

# 이동 : 가로, 세로 ,오른쪽 아래 대각선
dr = [0, 1, 1]
dc = [1, 0, 1]

result = 0

# 방향 = 가로 / 세로 / 대각선
direction = [0, 1, 2]

dfs([0,1], direction[0])

print(result)