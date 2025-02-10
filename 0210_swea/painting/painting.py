
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    territory = [[0] * 10 for _ in range(10)]    # 10 * 10 격자

    painting_num = int(input())            # 칠할 영역의 개수

    for num in range(painting_num):                             # 영역 갯수만큼 칠함
        painting = list(map(int,input().strip().split()))       # 영역 칠함
        for i in range(painting[0], painting[2]+1):              # 칠해지는 행
            for j in range(painting[1], painting[3]+1):          # 칠해지는 열
                territory[i][j] += painting[4]                  # painting 리스트 인덱스[4]는 색깔

    purple = 0          #territory 구역이 3이면 보라색임

    for i in range(10):      # 영역 다 돌면서 보라색 찾음
        for j in range(10):
            if territory[i][j] == 3:
                purple += 1


    print(f"#{test_case} {purple}")




    # ///////////////////////////////////////////////////////////////////////////////////


