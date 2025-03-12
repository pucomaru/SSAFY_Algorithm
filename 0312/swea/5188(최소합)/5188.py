#
# import sys
# sys.stdin = open("5188_input.txt", "r")

# 문제 포인트 : [0][0] 에서 [N-1][N-1]까지 오른쪽, 아래로만 움직일 수 있고 지나온 인덱스들의 최소합을구하자
# 완전탐색하면됨 DFS 이용
# 메모리를 효율적으로 쓰기 위해 백트래킹 이용

# 지금 있는 인덱스 , 지금까지 지나온 인덱스의 합 매개변수로 받음
def dfs(i, j, hap):
    global min_sum

    if i == N-1 and j == N-1:
        if hap < min_sum:
            min_sum = hap
            return

    # 최소합을 구하는 것이기때문에 지금까지 구한 최소합보다 크면 더 볼 가치가 없음
    if hap >= min_sum:
        return

    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        # hap 더 해준 것을 dfs하고 안 빼주면 다음 델타 합 dfs에 영향을 주므로 꼭 빼줘야 함
        if 0 <= ni < N and 0 <= nj < N:
            hap += numbers[ni][nj]
            dfs(ni, nj, hap)
            hap -= numbers[ni][nj]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                # N 가로 세로 칸 수
    numbers = [list(map(int,input().split())) for _ in range(N)]

    # 오른쪽이랑 아래로만 움직일 수 있음
    di = [0, 1]         # 우, 하
    dj = [1, 0]

    min_sum = 1e9

    dfs(0, 0, numbers[0][0])

    print(f"#{test_case} {min_sum}")
    # ///////////////////////////////////////////////////////////////////////////////////
