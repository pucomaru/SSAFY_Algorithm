# from itertools import combinations

def dfs(i, k):
    if i == N // 2:     # 음식 종류 두개로 나누어지면 최솟값 계산


    if visited[i] != 1:
        visited[i] = 1
        dfs(i+1,k+1)
        visited[i] = 0 





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                    # 식재료 개수

    food = [list(map(int,input().split())) for _ in range(N)]             # 음식 시너지
    visited = [0] * N

    dfs(0, 0)

    print(f"{test_case} {taste_minimum}")
    # ///////////////////////////////////////////////////////////////////////////////////


