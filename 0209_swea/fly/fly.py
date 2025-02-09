import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N , M = map(int,input().split())           # N * N 배열 / M * M 크기 파리채

    total_space = []            # 파리의 개수 입력한 2차원 배열
    max_catch = 0               # 잡은 파리 최대값

    for i in range(N):        # 2차원 배열에 파리 개수 입력
        fly_amount = list(map(int,input().split()))
        total_space.append(fly_amount)

    for i in range(N-M+1):       # 행
        for j in range(N-M+1):   # 열
            sum_catch = 0  # 잡은 파리 합
            for x in range(M):
                for y in range(M):
                    sum_catch += total_space[i+x][j+y]
                if sum_catch > max_catch :
                    max_catch = sum_catch





    print(f"#{test_case} {max_catch}" )



    # ///////////////////////////////////////////////////////////////////////////////////
