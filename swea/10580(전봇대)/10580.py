
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                            # 전선의 개수 N
    H = []                                      # 전선 N개 고도
    for i in range(N):
        H.append(list(map(int, input().split())))

    cross = 0
    i = 0

    while i < N-1:
        for a in range(1, N-i):
            if H[i][0] < H[i+a][0] and H[i][1] > H[i+a][1]:
                cross += 1

            elif H[i][0] > H[i+a][0] and H[i][1] < H[i+a][1]:
                cross += 1

        i += 1

    print(f"#{test_case} {cross}")
    # ///////////////////////////////////////////////////////////////////////////////////
