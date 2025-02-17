
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                        # 신청서 N개
    time = [list(map(int, input().split())) for _ in range(N)]      #  작업시간 s, 종료시간 e N개
    # [[20, 23], [17, 20], [23, 24], [4, 14], [8,18]]

    end_short_idx= 0
    for i in range(1, N):
        if time[i][1] < time[i][end_short_idx]:
            end_short_idx = i





    # ///////////////////////////////////////////////////////////////////////////////////
