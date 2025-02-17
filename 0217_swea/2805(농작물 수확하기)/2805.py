T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):

    N = int(input())                    # N * N 크기 농장

    crop = [input() for _ in range(N)]

    middle_row = N // 2                 # 5 * 5면 row idx 2 가 가운데줄

    crop_sum = 0                        # 농작물 가치 합

    i = 0
    for row in range(middle_row, -1, -1):   # 중간 행을 기준으로 중간 행 포함 윗줄 더하기
        for col in range(0+i, N-i):
            crop_sum += int(crop[row][col])
        i += 1

    i = 1
    for row in range(middle_row + 1, N):    # 중간 행을 기준으로 중간 행 포함안하고 아랫줄 더하기
        for col in range(0 + i, N - i):
            crop_sum += int(crop[row][col])
        i += 1

    print(f"#{test_case} {crop_sum}")

    # ///////////////////////////////////////////////////////////////////////////////////
