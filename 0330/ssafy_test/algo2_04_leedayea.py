# import sys
# sys.stdin = open('algo2_sample_in.txt', 'r')

# 누전 차단기와 콘센트를 최소한의 거리로 다 이어야하는 문제 (MST문제)
# 전선이 많아질 수도 있으므로 prim 알고리즘을 이용하는게 적합해보임.

import heapq

T = int(input())

def prim(d, c):

    # 한번 들린 정점 안들리게 하기 위한 리스트
    visited = [0] * (N + 1)

    # 누전 차단기부터 시작 / (전선 길이 , 리스트 con idx)
    pq = [(0, 0)]

    while pq:
        # print(visited)

        # 누전 차단기, 콘센트 다 들렸으면 끝
        if c == N + 1:
            return d

        # 제일 짧은 전선 부터 봄
        dist, node = heapq.heappop(pq)
        visited[node] = 1
        c += 1
        d += dist

        for new_dist, next_node in distance[node]:
            # 한번 들린 정점은 방문하면 안됨
            if visited[next_node] == 1:
                continue

            heapq.heappush(pq, [new_dist, next_node])

for tc in range(1, T+1):

    # N : 콘센트의 개수
    N = int(input())

    # 누전차단기와 콘센트 좌표들 담을 리스트 (0,0)은 누전차단기 위치
    con = [(0, 0)]

    # N개의 콘센트 좌표들
    for i in range(N):
        con.append(list(map(int, input().split())))

    # 전선과 전선, 전선과 누전 차단기의 거리를 담을 리스트
    distance = [[] * len(con) for _ in range(len(con))]

    for i in range(len(con)-1):
        for j in range(i + 1, len(con)):
            dis = abs(con[i][0] - con[j][0]) + abs(con[i][1] - con[j][1])
            distance[i].append([dis, j])
            distance[j].append([dis, i])

    # 거리 , 정점 몇개 들렸는지
    result = prim(0, 0)

    print(f"#{tc} {result}")