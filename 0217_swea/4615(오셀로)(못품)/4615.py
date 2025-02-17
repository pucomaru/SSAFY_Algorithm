

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())                    # 보드 길이 N * N ( 4, 6, 8 중 하나 ) / 돌을 넣는 횟수 M

    white = 0                           # 백돌
    black = 0                           # 흑돌

    board = [[" "] * N for _ in range(N)]       # 보드 세팅
    middle = N // 2
    board[middle-1][middle-1] = "1"             # 보드 시작 돌 설치
    board[middle-1][middle] = "2"
    board[middle][middle-1] = "2"
    board[middle][middle] = "1"

    print(board)

    for i in range(M):                                           # 게임 시작!
        put = list(map(str, input().split()))                    # 어디에 무슨 색 돌? ( 행, 열 , 돌색)
        row = int(put[0]) - 1                                         # 인덱스랑 위치 헷갈리지 않게 미리 - 1
        col = int(put[1]) - 1
        color = put[2]

        board[row][col] = color                                  # 돌을 놓는다.

        # 놓은 돌 위치 가로 확인
        # 가로확인 할 때 왼쪽 확인
        for i in range(1, col + 1 ):
            if board[row][col- i] == " ":                      # 왼쪽 칸 빈칸을 만나면 영향을 줄 수 없음.
                break
            elif board[row][col] - board[row][col - i] == 0:     #



        # 가로확인 할 때 오른쪽 확인
        for x in range(col, N):
            board[row][x]:

        # 놓은 돌 위치 세로 확인
        # 세로확인 할 때 위쪽 확인

        # 세로확인 할 때 아래쪽 확인



        # 놓은 돌 위치 대각선 확인
        # 대각선 확인 할 때  왼쪽 위 방향 확인
        # 대각선 확인 할 때  오른쪽 아래 방향 확인

        # 놓은 돌 위치 역대각선 확인
        # 역대각선 확인 할 때 오른쪽 위 방향 확인
        # 역대각선 확인 할 때 왼쪽 아래 방향 확인


    for i in range(N):                                          # 게임 끝! 흑돌 백돌 세보자
        for j in range(N):
            if board[i][j] == 1:
                white += 1
            elif board[i][j] == 0:
                black += 1

print(f"#{test_case} {black} {white}")



    # ///////////////////////////////////////////////////////////////////////////////////
