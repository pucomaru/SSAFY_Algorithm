
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())        # 길이 입력

    a_list = input().split()
    b_list = input().split()

    if N > M :                             # 보기 편하게 a_list를 짧은 줄로 고정
        N , M = M , N
        a_list,b_list = b_list, a_list

    max_sum = -1000000
    for num in range(M-N+1):    # 짧은 줄 인덱스 옮김
        gop_sum = 0
        for i in range(N):  # 짧은 줄 갯수 = 곱 횟수
            gop_sum += int(a_list[i]) * int(b_list[i+num])
        if gop_sum > max_sum:
            max_sum = gop_sum

    print(f"#{test_case} {max_sum}")



    # ///////////////////////////////////////////////////////////////////////////////////
