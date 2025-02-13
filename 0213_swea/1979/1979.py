
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, K = map(int,input().strip().split())         # N은 퍼즐 크기 / K는 단어의 길이

    puzzle = [list(map(int,input().strip().split())) for _ in range(N)]

    total_count = 0

    for width in range(N):                                          # 행 먼저 돌면서 값이 1인 칸 카운트세고 idx+1 이 1이 아닐경우 카운트가 단어길이와 같을 시 total_count + 1 
        count = 0                                                   
        for height in range(N-1):                                   # range(N)까지하면 height가 마지막 칸에 갔을 때 idx 오류가 날 수도 있느니 N-1 까지만 돌려주고 height가 N-1일 경우 따로 조건문 생성 
            if puzzle[width][height] == 1:
                count += 1
                if count == K and puzzle[width][height+1] != 1:
                    total_count += 1
                    count = 0
            if puzzle[width][height] == 0:
                count = 0
            if height + 1 == N - 1:
                if puzzle[width][height+1] == 1:
                    count += 1
                    if count == K:
                        total_count +=1

    for height in range(N):
        count = 0
        for width in range(N - 1):
            if puzzle[width][height] == 1:
                count += 1
                if count == K and puzzle[width + 1][height] != 1:
                    total_count += 1
                    count = 0
            if puzzle[width][height] == 0:
                count = 0
            if width + 1 == N - 1:
                if puzzle[width + 1][height] == 1:
                    count += 1
                    if count == K:
                        total_count += 1

    print(f"#{test_case} {total_count}")

# ///////////////////////////////////////////////////////////////////////////////////
