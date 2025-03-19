import sys
sys.stdin = open("5209_input.txt", "r")

def dfs(visit, charge, idx):
    global min_amount
    # idx를 벗어나면 최소 생산 비용 갱신
    if idx >= N:
        if charge < min_amount:
            min_amount = charge
            return

    # 계산하는 과정중 이미 갱신된 최소 비용보다 더 높으면 더 계산할 가치가 없음
    if idx < N and charge > min_amount:
        return

    # i 는 공장 / idx는 제품
    for i in range(N):
        # 한번 들린 공장은 못들림
        if i not in visit:
            charge += V[idx][i]
            visit.append(i)
            dfs(visit, charge, idx+1)
            charge -= V[idx][i]
            visit.pop()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                                 # N 제품 수
    V = [list(map(int, input().split())) for _ in range(N)]          # 생산 비용들

    min_amount = 1e9

    dfs([], 0, 0)

    print(f"#{test_case} {min_amount}")

    # ///////////////////////////////////////////////////////////////////////////////////
