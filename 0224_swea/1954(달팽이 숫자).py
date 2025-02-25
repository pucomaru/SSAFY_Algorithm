T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    space = [[0] * N for _ in range(N)]
    num = 1
    top, bottom = 0, N - 1
    left, right = 0, N - 1

    while num <= N * N:
        # 왼쪽 → 오른쪽
        for j in range(left, right + 1):
            space[top][j] = num
            num += 1
        top += 1

        # 위쪽 → 아래쪽
        for i in range(top, bottom + 1):
            space[i][right] = num
            num += 1
        right -= 1

        # 오른쪽 → 왼쪽
        if top <= bottom:
            for j in range(right, left - 1, -1):
                space[bottom][j] = num
                num += 1
            bottom -= 1

        # 아래쪽 → 위쪽
        if left <= right:
            for i in range(bottom, top - 1, -1):
                space[i][left] = num
                num += 1
            left += 1

    print(f"#{test_case}")
    for row in space:
        print(" ".join(map(str, row)))

# 나중에 다시 풀어보기