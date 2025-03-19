
import sys
sys.stdin = open("5247_input.txt", "r")

def dfs(v,cnt):
    global min_cnt

    if cnt > min_cnt:
        return

    if v == M:
        if cnt < min_cnt:
            min_cnt = cnt
            return

    # V가 M보다 작을 경우
    if v > M and v % 10 >= 1:
        dfs(v-10, cnt+1)

    if v > M and v % 10 < 1:
        dfs(v-1, cnt+1)

    # V가 M보다 클 경우
    if v < M and v * 2 <= M:
        dfs(v*2, cnt + 1)




    elif v > M:
        dfs(v-1, cnt + 1)
        dfs(v-10, cnt + 1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())                 # N = 자연수 / M = 만들어야 하는 자연수

    min_cnt = 1e9

    dfs(N, 0)

    print(f"#{test_case} {min_cnt}")
    # ///////////////////////////////////////////////////////////////////////////////////
