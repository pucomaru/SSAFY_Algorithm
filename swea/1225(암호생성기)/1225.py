
#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())                                    # 테스트 케이스
    password = deque(map(int,input().split()))

    num = 1                        # 감소 숫자
    while 1:
        if password[7] <= 0:
            break
        pop_num = password.popleft()
        pop_num -= num
        password.append(pop_num)
        num += 1
        if num > 5:
            num = 1

    password[7] = 0
    print(f"#{tc} {' '.join(map(str,password))}")

    # ///////////////////////////////////////////////////////////////////////////////////
