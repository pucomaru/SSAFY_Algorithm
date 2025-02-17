
import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                        # 격자의 크기
    ballon = [list(map(int,input().split())) for _ in range(N)]             # 풍선 점수

    score = [[0] * N for _ in range(N) ]                                    # 각 칸 점수 저장
    min_difference = 0                                                           # 최대 점수

    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]                                                       # x, y 증가량
    change = list(zip(x, y))
    # change = [(0, 1), (1, 0), (0, -1), (-1, 0)]                           # 변화량

    for row in range(N):                                                    # 모든 칸 풍선 점수 저장
        for col in range(N):
            amount = ballon[row][col]
            for dx, dy in change:
                for i in range(1, N):
                    nx = row + dx * i
                    ny = col + dy * i
                    if 0 <= nx < N and 0 <= ny < N:
                        amount += ballon[nx][ny]
            score[row][col] = amount

    max_sum = score[0][0]
    min_sum = score[0][0]

    for row in range(len(score)):
        for col in range(len(score)):
            if score[row][col] > max_sum:
                max_sum = score[row][col]
            if score[row][col] < min_sum:
                min_sum = score[row][col]

    min_difference = max_sum - min_sum                                  # 제일 큰 차이는 제일 큰 값에서 제일 작은 값 빼기

    print(f"#{test_case} {min_difference}")







    # ///////////////////////////////////////////////////////////////////////////////////
