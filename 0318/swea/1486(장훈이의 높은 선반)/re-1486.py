
import sys
sys.stdin = open("input (7).txt", "r")

def dfs(hap, idx):
    global result

    if hap >= B:
        result.append(hap)
        return

    if idx >= N:
        return

    dfs(hap + heights[idx], idx+1)
    dfs(hap, idx+1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, B = map(int, input().split())            # N : 점원의 수 / B: 선반 높이
    heights = list(map(int, input().split()))   # 점원의 키

    heights.sort(reverse=True)

    result = []

    min_difference = 1e9

    dfs(0, 0)

    value = min(result)

    resultresult = value - B
    print(f"#{test_case} {resultresult}")
    # ///////////////////////////////////////////////////////////////////////////////////
