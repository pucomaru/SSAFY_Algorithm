# gpt 도움 안받음 근데 구글에 역대각선 합 구하는 방법 찾아봄봄


import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    case= int(input())

    dimension_2 = []
    for n in range(100):        # 2차원 배열 생성
        width = list(map(int,input().split()))
        dimension_2.append(width)

    max_sum = 0         # 합 최댓값

    for width in range(len(dimension_2)):   # 행 최댓값
        width_sum = 0
        for height in range(len(dimension_2)):
            width_sum += dimension_2[width][height]
        if width_sum >= max_sum:
            max_sum = width_sum

    for height in range(len(dimension_2)):  # 열 최댓값
        height_sum = 0
        for width in range(len(dimension_2)):
            height_sum += dimension_2[width][height]
        if height_sum >= max_sum:
            max_sum = height_sum

    diagonal_sum = 0  # 대각선 합

    for i in range(len(dimension_2)):       #대각선 최댓값
        diagonal_sum += dimension_2[i][i]
    if diagonal_sum >= max_sum:
        max_sum = diagonal_sum

    reverse_diagonal_sum = 0 # 역대각선 합\

    for i in range(len(dimension_2)):
        reverse_diagonal_sum += dimension_2[i][100-1-i]
    if reverse_diagonal_sum >= max_sum :
        max_sum = reverse_diagonal_sum

    print(f"#{case} {max_sum}")





    # ///////////////////////////////////////////////////////////////////////////////////
