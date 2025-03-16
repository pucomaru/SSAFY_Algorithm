#import sys
#sys.stdin = open("input.txt", "r")

operator = ['-', '+', '*', '/']

def post_order(r):
    if r == 0:
        return 0

    left_value = post_order(left[r])
    right_value = post_order(right[r])

    if calculate[r] not in operator:
        return calculate[r]

    if calculate[r] == '+':
        return left_value + right_value
    elif calculate[r] == '-':
        return left_value - right_value
    elif calculate[r] == '*':
        return left_value * right_value
    elif calculate[r] == '/':
        return int(left_value / right_value)

for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                    # N 정점의 개수

    calculate = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    parent = [0] * (N+1)

    # N 줄에 걸쳐 정점의 정보가 주어짐
    # 정점이 정수면 정점 번호와 양의 정수
    # 정점이 연산자이면 정점 번호, 연산자, 해당 정점 왼쪽 자식, 오른쪽 자식 정점 번호
    for cnt in range(N):
        number = input().split()
        if len(number) == 4:
            calculate[int(number[0])] = number[1]
            left[int(number[0])] = int(number[2])
            right[int(number[0])] = int(number[3])
        elif len(number) == 2:
            calculate[int(number[0])] = int(number[1])

    result = post_order(1)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
