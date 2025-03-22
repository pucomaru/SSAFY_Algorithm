
import sys
sys.stdin = open("sample_input.txt", "r")

# 모든 노드를 다 들려야하는데 최소 가중치를 원한다?
# 프림 써야할듯 왜냐하면 노드, 간선 수가 많아 질 수도 있으니

import heapq

def prim(start):
    # 비용, 노드 첫 시작은 0
    pq = [(0, start)]
    visited = [0] * (V+1) # 방문 확인
    min_w = 0 # 최소 가중치 저장
    # 노드 들릴때마다 + 1
    count = 0

    # 모든 노드를 들릴 때까지
    while pq and count < V + 1:
        weight , node = heapq.heappop(pq)

        # 사이클 방지
        if visited[node] == 1:
            continue

        visited[node] = 1
        min_w += weight
        count += 1

        for next_node,cost in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq,(cost, next_node))

    return min_w

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    V, E = map(int,input().split())                 # V: 노드 번호 / E: 간선 개수
    # 인접 리스트 생성
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        # 시작, 도착, 가중치
        s, e, w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))

    # 출발점 임의로 0으로 설정 / 출발점 바꿔도 결과는 같
    result = prim(0)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
