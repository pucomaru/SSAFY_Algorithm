
#import sys
#sys.stdin = open("input.txt", "r")
def dfs(s, one, two):
    visited = [0] * 100
    stack = []
    pass_node = []
    possible = 0

    while 1:
        if visited[s] == 0:                  # 경로 탐색 시작
            visited[s] = 1
            pass_node.append(s)  # 지나온 노드 저장

        for i in one[s]:                     # 인접 리스트 돌면서 돌았는 지 확인
            if visited[i] == 0:              # 안돌았으면
                visited[i] = 1               # 돌아줌
                stack.append(s)              # 스택에 지나온 노드들 쌓음
                pass_node.append(i)          # 지나온 노드 저장
                s = i                        # 돌았으니까 시작 점 바꿈
                break
        else:
            for j in two[s]:
                if visited[j] == 0:  # 안돌았으면
                    visited[j] = 1  # 돌아줌
                    stack.append(s)  # 스택에 지나온 노드들 쌓음
                    pass_node.append(j)  # 지나온 노드 저장
                    s = j  # 돌았으니까 시작 점 바꿈
                    break
            else:                                # for - else 구문 / else 말고 if를 쓰면 for문을 빠져나와 실행되므로 꼭 for- else 구문!!
                if stack:                        # 스택에 지나온 노드를 다 탐색하면서 안 간 곳 있는 지 확인
                    s = stack.pop()
                else:                            # 다 확인했으면 break
                    break
    if 0 in pass_node and 99 in pass_node:
        possible = 1
        return possible
    else:
        return possible

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    tc, road_number = map(int, input().split())                    # 테스트 케이스 번호/ 길의 총 개수
    arr_one = [[] for _ in range(100)]                                           # 인접 리스트 1
    arr_two = [[] for _ in range(100)]                                           # 인접 리스트 2

    start = 0                                                      # 시작 지점

    road = list(map(int, input().split()))                         # 인접리스트에 정점 넣기
    for i in range(0,len(road),2):
        if len(arr_one[road[i]]) == 0:                             # 인접리스트1에 해당 정점 인접 칸이 비어져있다면 1이 삽입
            arr_one[road[i]].append(road[i+1])
        else:                                                      # 1에 값이 있다면 인접리스트 2에 삽입
            arr_two[road[i]].append(road[i+1])

    print(f"#{tc} {dfs(start, arr_one, arr_two)}")


    # ///////////////////////////////////////////////////////////////////////////////////
