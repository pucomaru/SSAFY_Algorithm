
import sys
sys.stdin = open("re_sample_input.txt", "r")

# 섬의 개수가 1 <= N <= 1000이니까 노드와 간선이 많아 질 수도 있으니
# Prim 알고리즘을 이용해야할 것 같음.
# 최소의 간선 수 or 최소 비용은 MST 문제

import heapq

def prim(E):

    # prim 알고리즘은 임의로 하나 선택해서 , 시작
    # 0번 섬을 임의로 선택해 시작하겠음
    # 비용 / 섬 번호 리스트에 삽입
    pq = [(0, 0)]
    # 이미 간 섬은 안가겠음
    visited = [0] * N

    # 비용 리스트 제일 적은 비용들로 갱신할 것이기 때문에 무한으로 다 설정
    cost = [float('inf')] * N
    # 임의로 선택한 섬은 비용없음
    cost[0] = 0

    min_cost = 0

    while pq:
        c, node = heapq.heappop(pq)

        # 이미 들린 섬은 확인할 필요없음
        if visited[node] == 1:
            continue

        visited[node] = 1
        min_cost += c

        for next_node in range(N):
            # visited 값이 1인건 이미 check 헀으므로 더 할 필요없음
            if visited[next_node] == 1:
                continue

            new_cost = ((x_coo[next_node] - x_coo[node]) ** 2 + (y_coo[next_node] - y_coo[node]) ** 2) * E
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    return min_cost

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                 # N 섬의 개수

    x_coo = list(map(int, input().split()))          # N개의 섬 x 좌표
    y_coo = list(map(int, input().split()))          # N개의 섬 y 좌표
    E = float(input())                               # E 환경부담금 세율

    result = prim(E)

    print(f"#{test_case} {round(result)}")
    # ///////////////////////////////////////////////////////////////////////////////////
