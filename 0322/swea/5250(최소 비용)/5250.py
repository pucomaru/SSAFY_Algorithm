
import sys
sys.stdin = open("5250_input.txt", "r")

# 항상 출발은 맨 왼쪽 위 / 도착지는 가장 오른쪽 아래
# 최소한의 연료 -> 목적지 도착 모든 칸을 들려야할 필요 없음
# 다익스트라 문제

import heapq

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra():
    # 최소 연료 소비량 쌓을 리스트
    dists= [[int(21e8)] * N for _ in range(N)]
    dists[0][0] = 0

    # 연료, 행, 열
    pq = [(0,0,0)]

    while pq:
        dist, y, x = heapq.heappop(pq)

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_y < N and 0 <= new_x < N:

                new_dist = 0

                if space[y][x] == space[new_y][new_x] or space[y][x] > space[new_y][new_x]:
                    new_dist = dists[y][x] + 1

                elif space[y][x] < space[new_y][new_x]:
                    new_dist = dists[y][x] + (space[new_y][new_x] - space[y][x]) + 1

                if dists[new_y][new_x] <= new_dist:
                    continue

                dists[new_y][new_x] = new_dist
                heapq.heappush(pq, (new_dist,new_y,new_x))

    return dists[N-1][N-1]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                # N * N 칸 크기
    space = [list(map(int,input().split())) for _ in range(N)]      # 연료 정보

    result = dijkstra()

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////

