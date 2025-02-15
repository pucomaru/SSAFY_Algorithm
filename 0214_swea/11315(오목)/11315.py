import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())  # 판 크기 N * N

    space = [input() for _ in range(N)]  # 오목 판

    result = "NO"

    # 가로 체크를 하자 (돌 연속해야함)
    # 행 한줄을 돌면서 값이 0인 인덱스 check 리스트에 추가 . check 내부에 저장한 인덱스 데이터를 ex = check = [1,2,3,4,5,6 .. ] 1,2,3,4,5 / 2,3,4,5,6 5개씩 짝을 지어서 처음과
    # 끝 차이를 본 다음에 만약 차이가 4라면 5개 짝지은게 연속이라는 뜻.
    for row in range(N):
        check = []  # 0 인덱스 저장
        for col in range(N):
            if space[row][col] == "o":
                check.append(col)

        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는 뜻
                result = "YES"
                break
        if result == "YES":
            break

    # 세로 체크를 하자 (연속 해야함)
    for col in range(N):
        check = []  # 0 인덱스 저장
        for row in range(N):
            if space[row][col] == "o":
                check.append(row)

        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는뜻
                result = "YES"
                break
        if result == "YES":
            break

    # 대각선 체크를 하자 (연속 해야함)
    for col in range(N):  # [0][0].... [0][N] 대각선 체크
        check = []
        for i in range(N):
            row = 0
            if col + i >= N or row + i >= N:
                break
            if space[row + i][col + i] == 'o':
                check.append(row + i)
        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는뜻
                result = "YES"
                break
        if result == "YES":
            break

    for row in range(1, N):  # [1][0]..... [N][0] 대각선 체크크
        check = []
        for i in range(N):
            col = 0
            if col + i >= N or row + i >= N:
                break
            if space[row + i][col + i] == 'o':
                check.append(row + i)
        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는뜻
                result = "YES"
                break
        if result == "YES":
            break

    # 역대각선 체크를 하자 (연속 해야함)
    for col in range(N - 1, -1, -1):  # [0][N-1].... [0][0] 대각선 체크
        check = []
        for i in range(N):
            row = 0
            if col - i < 0 or row + i >= N:
                break
            if space[row + i][col - i] == 'o':
                check.append(row + i)
        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는 뜻
                result = "YES"
                break
        if result == "YES":
            break

    for row in range(1, N):  # [1][N-1].... [N-1][N-1] 대각선 체크
        check = []
        for i in range(N):
            col = N - 1
            if col - i < 0 or row + i >= N:
                break
            if space[row + i][col - i] == 'o':
                check.append(row + i)
        for i in range(len(check) - 4):  # check 내 5개씩 짝 몇번 len(check) - 5 + 1
            if check[i + 4] - check[i] == 4:  # 처음과 끝 인덱스 차이가 4면 연속한다는 뜻
                result = "YES"
                break
        if result == "YES":
            break

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
