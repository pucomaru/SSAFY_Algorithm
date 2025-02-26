#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())             # N은 화덕의크기 M은 피자 개수
    cheese = list(map(int, input().split()))    # 피자에 뿌려진 치즈의 양

    fire = deque()                                   # 화로
    rest_pizza = deque()                             # 남은 피자
    melt_pizza = deque()                             # 녹은 피자

    for i in range(N):                               # 초기 화로 모습
        fire.append([cheese[i], i])

    for i in range(N, M):                             # 남은 피자
        rest_pizza.append([cheese[i], i])


    final = 0

    while 1:
        if len(melt_pizza) == M:
            final = melt_pizza[M-1][1]
            break

        for i in range(N):
            fire[i][0] //= 2
            if fire[i][0] == -1:
                continue
            if (fire[i][0] // 2) == 0 and len(rest_pizza) != 0:
                melt_pizza.append(fire[i])
                fire[i] = rest_pizza[0]
                rest_pizza.popleft()
            if (fire[i][0] // 2) == 0 and len(rest_pizza) == 0:
                melt_pizza.append(fire[i])
                fire[i][0] = -1

    print(f"#{test_case} {final+1}")
    # ///////////////////////////////////////////////////////////////////////////////////
