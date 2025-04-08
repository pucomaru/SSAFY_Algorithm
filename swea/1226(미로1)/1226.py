from collections import deque

def bfs(si, sj):
    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append([si,sj])
    visited[si][sj] = 1

    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1

        for i in range(4):
            ni = ti + di[i]
            nj = tj + dj[i]
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                q.append([ni,nj])
                visited[ni][nj] = 1
    return 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,  11):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())

    maze = [list(map(int,input().strip())) for _ in range(16)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    start = []
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start.append(i)
                start.append(j)

    # 도착할 수 있으면 1 / 못하면 0

    ans = bfs(start[0],start[1])
    print(f"#{tc} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////
