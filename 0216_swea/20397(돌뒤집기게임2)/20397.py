
import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())                # 돌의 수 N / 뒤집기 횟수 M
    start = input().split()                     # 초기 돌 상태
    change = [list(map(int,input().split())) for _ in range(M)]     # i 번째 돌 사이에 두고 마주보는 j개 돌 뒤집기 M번\
    # ex [[3,2],[5,3]....]

    for time in range(M):                           # 뒤집기 시작
        middle = change[time][0] - 1                # 가운데 돌 인덱스
        for i in range(1, change[time][1]+1):
            if middle - i >= 0 and middle + i < N:            # 가운데 돌 왼쪽 오른쪽 값이 있을때만 뒤집기.
                if int(start[middle-i]) == 1 and int(start[middle+i]) == 1:
                    start[middle-i] = 0
                    start[middle+i] = 0
                if int(start[middle - i]) == 0 and int(start[middle + i]) == 0a:
                    start[middle - i] = 1
                    start[middle + i] = 1




    print(f"#{test_case} {' '.join(map(str,start))}")







    # ///////////////////////////////////////////////////////////////////////////////////
