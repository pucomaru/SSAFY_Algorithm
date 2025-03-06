
#import sys
#sys.stdin = open("5176_input.txt", "r")


# 이진 탐색 트리 : 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브 트리 규칙
# -> 중위 순회를 돌면서 읽으면 해결될듯
# 일단 자연수 갯수 만큼 완전 이진 트리 형태로 만들어 주고 중위 순회 방식으로 숫자 읽음 .

def in_order(n):
    if n:
        in_order(left[n])
        number_in[n] = number.pop(0)
        in_order(right[n])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                # 자연수 1 ~ N
    V = N - 1                                       # 간선의 수

    # 6이면 [1,2,3,4,5,6]
    number = list(range(1, N+1))
    number_in = [0] * (N+1)

    left, right, parent = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)           # 왼쪽 자식, 오른쪽 자식, 부모 자식 리스트 만들기

    # 완전 이진 트리 형태 만들어 주기
    for i in range(1, N + 1):
        # 1일때는 부모 노드가 없으므로 부모 노드 없는 것만 설정
        if i == 1:
            parent[i] = 0
            continue
        # 짝수 번호 일경우 (왼쪽 자식)
        if i % 2 == 0:
            left[i//2] = i
            parent[i] = i//2
        # 홀수 번호 일 경우 (오른쪽 자식)
        if i % 2 == 1:
            right[i//2] = i
            parent[i] = i//2

    # 루트 찾아줌
    c = N
    while parent[c] != 0:
        c = parent[c]

    root = c

    in_order(root)

    print(f"#{test_case} {number_in[root]} {number_in[N//2]}")







    # ///////////////////////////////////////////////////////////////////////////////////
