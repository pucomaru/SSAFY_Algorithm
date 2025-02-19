# import sys
# sys.stdin = open("input.txt", "r")

def dfs(v, e, arr, s, g):
    visited = [0] * (v+1)
    stack = []
    pass_node = []
    result = 0

    while 1:
        if visited[s] == 0:                  # 경로 탐색 시작
            visited[s] = 1
            pass_node.append(s)  # 지나온 노드 저장

        for i in arr[s]:                     # 인접 리스트 돌면서 돌았는 지 확인
            if visited[i] == 0:              # 안돌았으면
                visited[i] = 1               # 돌아줌
                stack.append(s)              # 스택에 지나온 노드들 쌓음
                pass_node.append(i)          # 지나온 노드 저장
                s = i                        # 돌았으니까 시작 점 바꿈
                break
        else:                                # for - else 구문 / else 말고 if를 쓰면 for문을 빠져나와 실행되므로 꼭 for- else 구문!!
            if stack:                        # 스택에 지나온 노드를 다 탐색하면서 안 간 곳 있는 지 확인
                s = stack.pop()
            else:                            # 다 확인했으면 break
                break

    if s in pass_node and g in pass_node:    # 출발, 도착 노드 있는지 확인
        result = 1
        return result
    else:
        return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
# ///////////////////////////////////////////////////////////////////////////////////

    V, E = map(int, input().split())                # V개 노드, E개 간선
    graph = [[] for _ in range(V+1)]                # 인접리스트 생성

    for num in range(E):
        a, b = map(int,input().split())             # 인접 노드 리스트에 삽입
        graph[a].append(b)
    S, G = map(int,input().split())                 # 출발 노드 S / 도착 노드 G

    print(f"#{test_case} {dfs(V, E, graph, S, G)}")




# ///////////////////////////////////////////////////////////////////////////////////
