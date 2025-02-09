# gpt 도움 받음

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())       # 숫자 갯수
    numbers = list(map(int,input().split()))

    for nums in range(len(numbers) - 1):
        for num in range(len(numbers) - nums -1):
            if numbers[num] > numbers[num + 1]:
                numbers[num], numbers[num + 1] = numbers[num + 1], numbers[num]

    print(f"#{test_case} {' '.join(map(str,numbers))}")


    # ///////////////////////////////////////////////////////////////////////////////////
