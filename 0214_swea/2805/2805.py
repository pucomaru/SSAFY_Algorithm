import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())            # 농장의 크기

    crop = [input() for _ in range(N)]     # 농작물 가치 입력

    crop_sum = 0                # 수익 변수

    middle_idx = N // 2         # 중간 줄 인덱스

    # 가운데 행을 기준으로 위 아래 나눠서 따로 수익을 더 해준다.
    # 가운데 줄 기준 윗줄 쫙 더하기
    i = 1
    for width in range(middle_idx-1, -1, -1):         # 7 * 7 이면 width = 2, 1, 0 더하기
        for height in range(i, (N-i)):      # 중간 인덱스 인접 줄은 idx = 1 부터 시작 고정 뒤 idx도 고정
            crop_sum += int(crop[width][height])
        i += 1

    # for width in range(middle_idx-1, -1, -1):         # 7 * 7 이면 width = 2, 1, 0 더하기
    #     i = 1
    #     for height in range(i, (N-i)):      # 중간 인덱스 인접 줄은 idx = 1 부터 시작 고정 뒤 idx도 고정
    #         crop_sum += int(crop[width][height])
    #         i += 1
    # for height 문 내에다가 i를 넣으면 범위에 영향이 가서 원하는 결과가 안나옴

   # 가운데 줄 기준 가운데 줄 포함 아랫줄 쫙 더하기
    j = 0
    for width in range(N//2, N):                      # 7 * 7 이면 width = 3, 4, 5, 6 더하기
        for height in range(j, (N - j)):  # 중간 인덱스 인접 줄은 idx = 1 부터 시작 고정 뒤 idx도 고정
            crop_sum += int(crop[width][height])
        j += 1

    print(f"#{test_case} {crop_sum}")

    # ///////////////////////////////////////////////////////////////////////////////////
