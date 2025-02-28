
#import sys
#sys.stdin = open("input.txt", "r")

# 수정해야할 것 : delta 적용 / 리셋한 거 다시 원래대로 돌려줌ㅈ 


# 봉우리 높이 지도, 제일 높은 봉우리 인덱스가 시작, 최대 공사 깊이 , 자르는 횟수, 등산로 길이 cnt 매개변수로 받음
def dfs(map_info, p, k, cut, road):

    global N

    # 오른쪽 방향
    if 0 < p[0] < N and 0 < p[1]+1 < N :
        if map_info[p[0]][p[1]] > map_info[p[0]][p[1]+1]:                               # 만약 갈 수 있는 방향의 높이가 현재 위치보다 작다?
            save = map_info[p[0]][p[1]]                                                 # 왔던 곳 못간다고 지정하기전에 그 값 저장 
            map_info[p[0]][p[1]] = 21                                                   # 왔던 곳은 다시 못감
            p = [p[0], p[1]+1]                                                          # 등산로 가능 . 이동 가능
            road += 1
            dfs(map_info, p, k, cut, road)
            map_info[p[0]][p[1]] = save                                                 # 원래 맵 정보 망가뜨리지않음

        if map_info[p[0]][p[1]] <= map_info[p[0]][p[1]+1]:                              # 만약 갈 수 있는 방향의 높이가 현재 위치보다 크거나 같다?
            if cut == 1 and (map_info[p[0]][p[1]] + k > map_info[p[0]][p[1]+1])  :      # 공사 횟수가 남아있고 공사 후에 현재 위치보다 낮으면 고
                map_info[p[0]][p[1] + 1] = map_info[p[0]][p[1]] - 1                     # 갈 방향 봉우리 높이를 현재 위치보다 1 낮게 만듬
                cut = 0                                                                 # 이제 공사 불가능
                p = [p[0], p[1]+1]                                                      # 이동
                road += 1
                map_info[p[0]][p[1]] = 21                                               # 왔던 곳은 다시 못감
                dfs(map_info, p, k, cut, road)

    # 아래 방향
    if 0 < p[0] + 1 < N and 0 < p[1]< N :
        if map_info[p[0]][p[1]] > map_info[p[0]+1][p[1]]:                               # 만약 갈 수 있는 방향의 높이가 현재 위치보다 작다?
            map_info[p[0]][p[1]] = 21                                                   # 왔던 곳은 다시 못감
            p = [p[0]+1, p[1]]                                                          # 등산로 가능 . 이동 가능
            road += 1
            dfs(map_info, p, k, cut, road)
        if map_info[p[0]][p[1]] <= map_info[p[0]+1][p[1]]:                              # 만약 갈 수 있는 방향의 높이가 현재 위치보다 크거나 같다?
            if cut == 1 and (map_info[p[0]][p[1]] + k > map_info[p[0]+1][p[1]])  :      # 공사 횟수가 남아있고 공사 후에 현재 위치보다 낮으면 고
                map_info[p[0]+1][p[1]] = map_info[p[0]][p[1]] - 1                       # 갈 방향 봉우리 높이를 현재 위치보다 1 낮게 만듬
                cut = 0                                                                 # 이제 공사 불가능
                p = [p[0]+1, p[1]]                                                      # 이동
                road += 1
                map_info[p[0]][p[1]] = 21                                               # 왔던 곳은 다시 못감
                dfs(map_info, p, k, cut, road)

    # 왼쪽 방향
    if 0 < p[0] < N and 0 < p[1] - 1 < N :
        if map_info[p[0]][p[1]] > map_info[p[0]][p[1]-1]:                               # 만약 갈 수 있는 방향의 높이가 현재 위치보다 작다?
            map_info[p[0]][p[1]] = 21                                                   # 왔던 곳은 다시 못감
            p = [p[0], p[1]-1]                                                          # 등산로 가능 . 이동 가능
            road += 1
            dfs(map_info, p, k, cut, road)
        if map_info[p[0]][p[1]] <= map_info[p[0]][p[1]-1]:                              # 만약 갈 수 있는 방향의 높이가 현재 위치보다 크거나 같다?
            if cut == 1 and (map_info[p[0]][p[1]] + k > map_info[p[0]][p[1]-1])  :      # 공사 횟수가 남아있고 공사 후에 현재 위치보다 낮으면 고
                map_info[p[0]][p[1]-1] = map_info[p[0]][p[1]] - 1                       # 갈 방향 봉우리 높이를 현재 위치보다 1 낮게 만듬
                cut = 0                                                                 # 이제 공사 불가능
                p = [p[0], p[1]-1]                                                      # 이동
                road += 1
                map_info[p[0]][p[1]] = 21                                               # 왔던 곳은 다시 못감
                dfs(map_info, p, k, cut, road)

    # 위 방향
    if 0 < p[0] - 1 < N and 0 < p[1]< N :
        if map_info[p[0]][p[1]] > map_info[p[0]-1][p[1]]:                               # 만약 갈 수 있는 방향의 높이가 현재 위치보다 작다?
            map_info[p[0]][p[1]] = 21                                                   # 왔던 곳은 다시 못감
            p = [p[0]-1, p[1]]                                                          # 등산로 가능 . 이동 가능
            road += 1
            dfs(map_info, p, k, cut, road)
        if map_info[p[0]][p[1]] <= map_info[p[0]-1][p[1]]:                              # 만약 갈 수 있는 방향의 높이가 현재 위치보다 크거나 같다?
            if cut == 1 and (map_info[p[0]][p[1]] + k > map_info[p[0]-1][p[1]])  :      # 공사 횟수가 남아있고 공사 후에 현재 위치보다 낮으면 고
                map_info[p[0]-1][p[1]] = map_info[p[0]][p[1]] - 1                       # 갈 방향 봉우리 높이를 현재 위치보다 1 낮게 만듬
                cut = 0                                                                 # 이제 공사 불가능
                p = [p[0]-1, p[1]]                                                      # 이동
                road += 1
                map_info[p[0]][p[1]] = 21                                               # 왔던 곳은 다시 못감
                dfs(map_info, p, k, cut, road)

    # 지금 있는 칸에서 더이상 갈 곳이 없으면 지금까지 왔던 등산로 길이 append
    if ((p[1] + 1 < N and map_info[p[0]][p[1]] < map_info[p[0]][p[1] + 1]) or
            (p[0] + 1 < N and map_info[p[0]][p[1]] < map_info[p[0] + 1][p[1]]) or
            (p[0] - 1 >= 0 and map_info[p[0]][p[1]] < map_info[p[0] - 1][p[1]]) or
            (p[1] - 1 >= 0 and map_info[p[0]][p[1]] < map_info[p[0]][p[1] - 1])):
        return
    else:
        roads.append(road)
        return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, K = map(int,input().split())                # 지도 한 변의 길이 N / 최대 공사 가능 깊이 K

    map_information = [list(map(int,input().split())) for _ in range(N)]        # 지도 정보

    result = []                                                     # 가장 긴 등산로 길이
    peak = 0                                                        # 제일 높은 봉우리 높이
    peaks = []                                                      # 제일 높은 봉우리들
    cut_cnt = 1                                                     # 봉우리를 깎을 수 있는 횟수
    roads = []                                                      # 등산로 길이들 리스트
    road_start = 1                                                  # 등산로 시작 cnt

    # 제일 높은 봉우리 높이 찾음.
    for i in range(N):
        for j in range(N):
            if map_information[i][j] > peak:
                peak = map_information[i][j]
    # 제일 높은 봉우리 인덱스 찾음.
    for i in range(N):
        for j in range(N):
            if map_information[i][j] == peak:
                peaks.append([i,j])

    for start in peaks:
        dfs(map_information, start, K, cut_cnt, road_start)  # 제일 긴 등산로 값 받음

    result = max(roads)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
