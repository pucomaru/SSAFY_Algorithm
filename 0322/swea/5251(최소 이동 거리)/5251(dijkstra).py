
import sys
sys.stdin = open("sample_input (3).txt", "r")

# 다익스트라 버전
# 최소 거리 찾기

import heapq

def dijkstra(start):

    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0,start)]

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now] < cost:
            continue

        for next, weight in graph[now]:
            new_cost = cost + weight
            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(pq,(new_cost,next))

    return dist[N]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, E = map(int,input().split())         # N : 마지막 연결지점 / E: 도로
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))

    result = dijkstra(0)

    print(f"#{test_case} {result}")


    # ///////////////////////////////////////////////////////////////////////////////////
