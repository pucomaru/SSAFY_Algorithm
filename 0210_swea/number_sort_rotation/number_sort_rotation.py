
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())  # N * N 행렬

    number_list = [list(map(int, input().split())) for _ in range(number)]  # N * N 행렬 완성


    # 90도 회전

    rotation_90_number_list = list(zip(*number_list[::-1]))

    # 180도 회전
    rotation_180_number_list = list(zip(*rotation_90_number_list[::-1]))

    # 270도 회전
    rotation_270_number_list = list(zip(*rotation_180_number_list[::-1]))


    print(f"#{test_case}")

    for i in range(number):
        for j in range(number):
            print(rotation_90_number_list[i][j], end = '')
        print(end = ' ')
        for j in range(number):
            print(rotation_180_number_list[i][j], end = '')
        print(end = ' ')
        for j in range(number):
            print(rotation_270_number_list[i][j], end = '')
        print()




# ///////////////////////////////////////////////////////////////////////////////////
