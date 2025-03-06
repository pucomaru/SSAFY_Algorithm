from collections import deque
def bfs(si, sj):
    global N
    global now_i
    global now_j
    global get_in
    global min_time
    global monster_customer

    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ti, tj = q.popleft()
        for delta in range(4):
            ni = ti + di[delta]
            nj = tj + dj[delta]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ti][tj] + 1
                q.append([ni, nj])

    # visited에 거리 길이 정보 저장 .
    # 이제 제일 가까운 곳 찾아줌.
    near = 100000
    near_information = []

    pop_num = 0
    for num in range(len(monster_customer)):
        if visited[monster_customer[num][1]][monster_customer[num][2]] < near:
            if monster_customer[num][0] < 0 and abs(monster_customer[num][0]) not in get_in:
                continue
            near = visited[monster_customer[num][1]][monster_customer[num][2]]
            near_information = monster_customer[num]
            pop_num = num

    # 들린 곳 정해줌
    get_in.append(near_information[0])
    min_time += near - 1
    now_i = near_information[1]
    now_j = near_information[2]
    monster_customer.pop(pop_num)



T = int(input())
for test_case in range(1, T+1):
    #######################################################################################################
    N = int(input())                                                        # N * N 정사각형
    maps = [list(map(int, input().split())) for _ in range(N)]              # 맵 정보
    min_time = 0                                                            # 최소 시간

    di = [0, 1, 0, -1]                                                      # 델타 우하좌상 방향
    dj = [1, 0, -1, 0]
    # 시작 인덱스
    now_i = 0
    now_j = 0

    # 몬스터 번호 / 인덱스 ( i, j)
    monster_customer = []

    # 들린 곳
    get_in = []

    for i in range(N):
        for j in range(N):
            if maps[i][j] != 0:
                monster_customer.append([maps[i][j], i, j])

    # 몬스터 + 고객 있는 만큼 bfs 돌림
    for i in range(len(monster_customer)):
        bfs(now_i, now_j)
    if maps[0][0] == -3:
        min_time -= 1
    if maps[0][0] == 3:
        min_time -= 1
    print(f"#{test_case} {min_time}")




    