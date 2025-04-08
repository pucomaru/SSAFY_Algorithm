
import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())         # N은 전체 칸 크기 / M은 스프레이 범위
    fly_amount = [list(map(int,input().split())) for _ in range(N)]

    max_fly_catch = 0                       # 잡은 파리 최대 갯수
    # 십자 모양 잡기
    for row in range(N):
        for col in range(N):
            fly_catch = fly_amount[row][col]                       # 잡은 파리
            for i in range (1, M):
                if 0 <= col-i < N :
                    fly_catch += fly_amount[row][col-i]
                if 0 <= col + i < N:
                    fly_catch += fly_amount[row][col+i]
                if 0 <= row + i < N:
                    fly_catch += fly_amount[row+i][col]
                if 0 <= row - i < N:
                    fly_catch += fly_amount[row-i][col]
            if fly_catch > max_fly_catch:
                max_fly_catch = fly_catch

    # 대각선 모양 잡기
    for row in range(N):
        for col in range(N):
            fly_catch = fly_amount[row][col]                       # 잡은 파리
            for i in range (1, M):
                if 0 <= row-i < N and 0 <= col-i < N:
                    fly_catch += fly_amount[row-i][col-i]
                if 0 <= row+i < N and 0 <= col-i < N:
                    fly_catch += fly_amount[row+i][col-i]
                if 0 <= row-i < N and 0 <= col+i < N:
                    fly_catch += fly_amount[row-i][col+i]
                if 0 <= row+i < N and 0 <= col+i < N:
                    fly_catch += fly_amount[row+i][col+i]
            if fly_catch > max_fly_catch:
                max_fly_catch = fly_catch

    print(f"#{test_case} {max_fly_catch}")
    # ///////////////////////////////////////////////////////////////////////////////////
