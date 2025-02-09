# gpt 도움 안받음음

import sys
sys.stdin = open('input.txt','r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())       # 소인수분해할 정수
    prime = [0,0,0,0,0]         # 소인수 갯수 저장

    while True:
        if number % 2 == 0:
            prime[0] += 1
            number /= 2
        if number % 3 == 0:
            prime[1] += 1
            number /= 3
        if number % 5 == 0:
            prime[2] += 1
            number /= 5
        if number % 7 == 0:
            prime[3] += 1
            number /= 7
        if number % 11 == 0:
            prime[4] += 1
            number /= 11
        if number == 1:
            break

    print (f"#{test_case} {' '.join(map(str,prime))}")

    # ///////////////////////////////////////////////////////////////////////////////////
