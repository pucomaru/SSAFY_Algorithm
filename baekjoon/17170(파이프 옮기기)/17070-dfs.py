
# 방향 0 = 가로 , 1 = 세로 , 2 = 대각선

def dfs(end_i,end_j,dir):
    global result

    if end_i == N-1 and end_j == N-1:
        result += 1
        return

    if dir == 0:
        direction = [0,2]
    elif dir == 1:
        direction = [1,2]
    elif dir == 2:
        direction = [0,1,2]

    for d in direction:
        ni = end_i + di[d]
        nj = end_j + dj[d]

        if d == 2:
            if 0<= ni < N and 0 <= nj < N:
                if home[ni][nj] != 1 and home[ni-1][nj] != 1 and home[ni][nj-1] != 1:
                    dfs(ni, nj, d)
        elif d == 0:
            if 0 <= nj < N:
                if home[ni][nj] != 1:
                    dfs(ni, nj, d)
        elif d == 1:
            if 0 <= ni < N:
                if home[ni][nj] != 1:
                    dfs(ni, nj, d)

N = int(input())

home = [list(map(int, input().split())) for _ in range(N)]

result = 0

di = [0, 1, 1]
dj = [1, 0, 1]

# 스타트 인덱스 i,j / 방향
dfs(0,1,0)

print(result)
