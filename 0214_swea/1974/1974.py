
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 0                      # 결과 다 확인
    sudoku_result = 0

    # 행조건 확인
    for width in range(9):
        count_num = [0] * 9  # 1 - 9 숫자 다 하나만 있는 지 확인
        check = 0

        for height in range(9):
            count_num[(sudoku[width][height]) - 1] += 1

        for idx in count_num:
            if idx != 1:
                check = 1
                break

        if check == 1:
            break

        result += 1

    # 열조건 확인:
    for height in range(9):
        count_num = [0] * 9  # 1 - 9 숫자 다 하나만 있는 지 확인
        check = 0

        for width in range(9):
            count_num[(sudoku[width][height]) - 1] += 1

        for idx in count_num:
            if idx != 1:
                check = 1
                break

        if check == 1:
            break
        result += 1

    # 블럭 확인 :

    delta = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    for dx, dy in delta:
        count_num = [0] * 9  # 1 - 9 숫자 다 하나만 있는 지 확인
        # delta 를 대입할 때마다 초기화를 해줘야하니까 count_num 을 이 for 문에다가 초기화
        check = 0

        for width in range(3):
            for height in range(3):
                count_num[(sudoku[width+dx][height+dy]) - 1] += 1

        for idx in count_num:
            if idx != 1:
                check = 1
                break

        if check == 1:
            break

        result += 1

    if result == 27:
        sudoku_result = 1

    print(f"#{test_case} {sudoku_result}")
    # ///////////////////////////////////////////////////////////////////////////////////
