
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())            # 농장의 크기

    crop = [input() for _ in range(N)]     # 농작물 가치 입력

    print(crop)

    crop_sum = 0                # 수익 변수

    middle_idx = N // 2         # 중간 줄 인덱스

    # 가운데 행을 기준으로 위 아래 나눠서 따로 수익을 더 해준다.
    # 가운데 줄 기준 윗줄 쫙 더하기
    for width in range(middle_idx-1, -1, -1):         # 7 * 7 이면 width = 2, 1, 0 더하기
        for i in range(N // 2):                       # 몫 만큼 줄 계산 해야함
            for height in range(1 + i, (N-1-i)):      # 중간 인덱스 인접 줄은 idx = 1 부터 시작 고정 뒤 idx도 고정
                crop_sum += int(crop[width][height])

    # 가운데 줄 기준 가운데 줄 포함 아랫줄 쫙 더하기
    for width in range(N//2, N):                      # 7 * 7 이면 width = 3, 4, 5, 6 더하기
        for i in range(N // 2 + 1):                   # 중간 줄 포함해서 계산하므로 몫 + 1 계산함
            for height in range(1 + i, (N - 1 - i)):  # 중간 인덱스 인접 줄은 idx = 1 부터 시작 고정 뒤 idx도 고정
                crop_sum += int(crop[width][height])

    print(f"{test_case} {crop_sum}")

    # ///////////////////////////////////////////////////////////////////////////////////
