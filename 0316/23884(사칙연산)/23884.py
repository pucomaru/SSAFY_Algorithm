#import sys
#sys.stdin = open("input.txt", "r")

operators = {"+", "-", "*", "/"}


def post_order(node):
    if node == 0:  # 노드가 없으면 0 반환
        return 0

    # 왼쪽, 오른쪽 서브트리 값 계산
    left_value = post_order(left[node])
    right_value = post_order(right[node])

    # 숫자인 경우 (연산자 리스트에 없으면 숫자로 판단)
    if calculate[node] not in operators:
        return int(calculate[node])

    # 연산자 처리
    if calculate[node] == '+':
        return left_value + right_value
    elif calculate[node] == '-':
        return left_value - right_value
    elif calculate[node] == '*':
        return left_value * right_value
    elif calculate[node] == '/':
        return left_value / right_value

# 정점이 정수면 정점 번호와 양의 정수가 주어지고
# 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪾 자식, 오른쪽 자신의 정점 번호가 주어짐
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 중위 순회로 계산

for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                # 정점의 개수
    V = N - 1                                       # 간선

    left = [0] * (N + 1)                            # 왼쪽 자식 번호
    right = [0] * (N + 1)                           # 오른쪽 자식 번호
    calculate = [0] * (N + 1)                       # value 들 넣음
    stack = []

    for i in range(N):
        cal = input().split()
        p = int(cal[0])

        # 연산자일 경우는 정점 번호 , 연산자 , 정점 왼쪽 자식, 정점 오른쪽 자식 받음
        if len(cal) == 4:
            l_c = int(cal[2])
            r_c = int(cal[3])
            left[p] = l_c
            right[p] = r_c
            calculate[p] = cal[1]
        # 정수일 경우는 정점 번호, 양의 정수 받음
        if len(cal) == 2:
            calculate[p] = cal[1]


    result = int(post_order(1))

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
