
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    width, height = list(map(int,input().split()))           # 행의 갯수 / 열의 갯수


    flower_in_ballon = [list(map(int, input().split())) for _ in range(width)]      #  꽃가루 갯수입력

    flower_max = 0

    for i in range(width):                  # 상하좌우 꽃가루 갯수 더함
        for j in range(height):
            flower_sum = flower_in_ballon[i][j]
            for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                new_i = i + di
                new_j = j + dj

                if 0 <= new_i < width and 0 <= new_j < height:
                    flower_sum += flower_in_ballon[new_i][new_j]

            if flower_sum >= flower_max:
                flower_max = flower_sum


    print(f"#{test_case} {flower_max}")



    # ///////////////////////////////////////////////////////////////////////////////////
