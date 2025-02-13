import sys
sys.stdin = open("bracket_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    line = input()

    left = []  # "(" 담을 리스트
    right = []  # ")" 담을 리스트
    result = 0

    for i in range(len(line)):
        if line[i] == "(":
            left.append(line[i])
        if line[i] == ")":
            right.append(line[i])

    if len(left) == len(right):
        result = 1
    else:
        result = -1

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
