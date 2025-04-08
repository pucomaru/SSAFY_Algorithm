
import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    width, height = list(map(int, input().strip().split()))            # 행 열 구함

    space = []                      # 꽃가루 갯수 공간

    for num in range(width):        # width (행) 번 꽃가루 대입
        space.append(list(map(int, input().strip().split())))


    # 꽃가루 공간 완성 이제 최대값 구해야함

    di = [0, 1, 0, -1]      # 행 변화값
    dj = [1, 0, -1, 0]      # 얄 변화값

    max_sum = 0             # 최대값 구함

    for i in range(width):
        for j in range(height):
            result = space[i][j]                    # 추가 터짐 횟수 / 가운데 값 
            for number in range(1, result+1):
                for ni, nj in list(zip(di, dj)):
                    if 0 <= i + ni*number <= width - 1 and 0 <= j + nj*number <= height - 1:
                        result += space[i + ni*number][j + nj*number]

            if result > max_sum:
                max_sum = result

    print(f"#{test_case} {max_sum}")

    # ///////////////////////////////////////////////////////////////////////////////////
