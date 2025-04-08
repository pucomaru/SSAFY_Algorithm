import sys
sys.stdin = open("input (7).txt", "r")

# 확률은 곱할수록 더 확률 낮아짐

def dfs(s, total):
    global max_success
    global visited

    # 0일때 계속 곱하면 의미없는 행동 반복됨
    if total == 0:
        return

    # 가지치기
    if total * 100 < max_success:
        return

    # 직원이랑 일 매칭 다 해주면 최대값 갱신
    if s >= N:
        if total * 100 > max_success:
            max_success = total * 100
            return

    # dfs
    for j in range(N):
        if visited[j] != 1:
            visited[j] = 1
            dfs(s+1, total * (success[s][j] * 0.01))
            visited[j] = 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                # 직원들의 번호, 직원들 해야할 일
    success = [list(map(int, input().split())) for _ in range(N)]    # I번 직원이 J 일을 하면 성공할 확률

    visited = [0] * N

    max_success = -1

    # 시작 직원수 , total 합
    dfs(0, 1)

    print(f"#{test_case} {max_success:.6f}")
    # ///////////////////////////////////////////////////////////////////////////////////
