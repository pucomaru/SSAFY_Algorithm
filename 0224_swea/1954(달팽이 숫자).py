
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N = int(input())                    # 달팽이 크기

    dx = [1, 0  -1, 0]                  # x 증가량
    dy = [0, 1, 0, -1]                  # y 증가량
    delta = list(zip(dx,dy))            # 델타

    space = [[0] * N for _ in range(N)]         # 공간


    num = 1
    while 1:
        if num > N*N:
            break

        i = 0
        j = 0

        for right in range(N):
            space[i][j] = num
            i += 1
            num += 1
        for down in range(N-1):
            j += 1
            space[i][j] = num
            num += 1
        for left in range(N-1):
            i -= 1
            space[i][j] = num
            num += 1
        for up in range(N-2):
            j -= 1
            space[i][j] = num
            num +=1

        N /= 2

    print(f"{test_case} {}")
    # ///////////////////////////////////////////////////////////////////////////////////
