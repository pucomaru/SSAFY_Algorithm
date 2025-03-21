
import sys
sys.stdin = open("re_sample_input.txt", "r")

# 섬의 개수가 1 <= N <= 1000이니까 Prim 알고리즘을 이용해야할 것 같음 .
# 최소의 간선 수 or 최소 비용은 MST 문제

import heapq

def prim(E):

    # 처음 시작할 섬 (비용, 섬번호) 삽입
    pq = [(0,0)]
    # 한번 간 섬은 안감
    visited = [0] * N
    # 최소 비용
    min_cost = 0

    # 섬에 가는 간선 중 젤 낮은 비용 입력할 리스트
    dists = [float('inf')] * N
    # 첫 섬은 0
    dists[0] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node] == 1:
            continue

        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            new_cost = ((x_coo[next_node] - x_coo[node]) ** 2 + ((y_coo[next_node] - y_coo[node]) ** 2)) * E

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                 # N 섬의 개수

    x_coo = list(map(int, input().split()))          # N개의 섬 x 좌표
    y_coo = list(map(int, input().split()))          # N개의 섬 y 좌표
    E = float(input())                               # E 환경부담금 세율

    result = prim(E)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
