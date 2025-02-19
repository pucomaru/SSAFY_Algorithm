
#import sys
#sys.stdin = open("graph_input.txt", "r")

def dfs(start, v, arr):                             # start = 시작 정점 / v = 정점의 갯수 / arr = 인접 리스트
    visited = [0] * (v+1)                           # 방문했는지 안했는지 체크하는 리스트
    stack = []                                      # stack에다가 지난 정점 쌓음.
    pop_list = []
    while True:
        if not visited[start]:
            visited[start] = 1
            pop_list.append(start)

        for pass_point in adj_list[start]:         # 인접 리스트 돌면서 안 돈 리스트 체크 .
            if not visited[pass_point]:
                stack.append(start)
                start = pass_point
                break

        else:
            if stack:
                start = stack.pop()

            else:
                break

    return pop_list

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////

    V, E = map(int, input().split())                    # V = 정점의 개수 / E = 간선의 개수
    connect = list(map(int, input().split()))           # 간선의 개수 만큼 연결된 두 정점
    adj_list = [[] for i in range(V+1)]                 # 인접 리스트 생성

    for i in range(E):
        a, b = connect[2 * i] , connect[1 + (2 * i)]    # 인접한 원소들 확인
        adj_list[a].append(b)                           # 인접한 원소들 인접한 리스트에 대입
        adj_list[b].append(a)

    print(f"#{test_case} {'-'.join(map(str,dfs(1, V, adj_list)))}")
    # ///////////////////////////////////////////////////////////////////////////////////
