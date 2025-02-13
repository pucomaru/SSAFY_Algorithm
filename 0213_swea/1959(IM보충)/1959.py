
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().strip().split())             # 숫자열 숫자 갯수

    line_a = list(map(int,input().strip().split()))     # 첫번째 줄
    line_b = list(map(int,input().strip().split()))     # 두번째 줄

    if N > M :
        long = line_a
        short = line_b
    else :
        long = line_b
        short = line_b

    max_sum = 0                                         # 곱 합한거 최댓값

    for i in range(len(long) - len(short) + 2):
        sum = 0
        for j in range(len(short)):
            sum += short[j] * long[j+i] 
        if sum > max_sum:
            max_sum = sum

        




    print(f"{test_case} {max_sum}")
    # ///////////////////////////////////////////////////////////////////////////////////
