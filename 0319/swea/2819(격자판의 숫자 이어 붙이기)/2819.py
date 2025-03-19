
import sys
sys.stdin = open("sample_input (7).txt", "r")

def dfs(si,sj,number):
    # 중복 제거를 위해 집합을 이용하고 튜플로 넣음 집합은 변경 할 수 없는 객체?만 요소로 받음
    if len(number) == 7:
        seven.add(tuple(number))
        return

    for d in range(4):
        ni = si + dx[d]
        nj = sj + dy[d]
        if 0 <= ni < N and 0 <= nj < N:
            number.append(space[ni][nj])
            dfs(ni, nj, number)
            number.pop()    # 백트래킹

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = 4                                                           # 격자판은 4 * 4 크기
    space = [input().split() for _ in range(N)]                     # 격자판 숫자들

    seven = set()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            dfs(i, j, [space[i][j]])

    print(f"#{test_case} {len(seven)}")

    # ///////////////////////////////////////////////////////////////////////////////////
