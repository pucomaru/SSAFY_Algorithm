# 지피티 풀이이

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][dir]: (i,j) 위치에 dir 방향으로 파이프가 올 수 있는 경우의 수
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 시작: (0,1)에 가로 파이프

for i in range(N):
    for j in range(2, N):  # (0,2)부터 시작
        if home[i][j] == 1:
            continue

        # 가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] if home[i][j-1] == 0 else 0

        # 세로
        if i > 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] if home[i-1][j] == 0 else 0

        # 대각선
        if i > 0 and home[i-1][j] == 0 and home[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2] if home[i-1][j-1] == 0 else 0

# 결과는 끝 위치에 어떤 방향으로 오든 모두 합한 것
print(sum(dp[N-1][N-1]))