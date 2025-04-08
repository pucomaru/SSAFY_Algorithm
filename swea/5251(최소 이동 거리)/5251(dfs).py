
import sys
sys.stdin = open("sample_input (3).txt", "r")


def dfs(start,distance):
    global min_dist

    if distance > min_dist:
        return

    if start == N:
        if distance < min_dist:
            min_dist = distance

    for e, d in connect[start]:
        dfs(e,distance + d)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # N : 마지막 연결지점 번호 / E: 도로의 개수
    N, E = map(int,input().split())

    # 구간 시작 s, 구간 끝 지점 e, 구간 거리 w
    road = [list(map(int,input().split())) for _ in range(E)]

    connect = [[] for _ in range(N+1)]

    min_dist = 1e9

    for s,e,w in road:
        connect[s].append([e,w])

    dfs(0,0)

    print(f"#{test_case} {min_dist}")

    # ///////////////////////////////////////////////////////////////////////////////////
