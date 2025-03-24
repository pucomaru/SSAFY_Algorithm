# dfs로 푸니까 시간초과 뜸
# DP로 구현
# 최소 값 저장하면서 나감

# N : 물품의 수 / K : 준서가 버틸 수 있는 무게
N, K = map(int, input().split())

# N개의 물건들 무게 W와 가치 V
items = [list(map(int, input().split())) for _ in range(N)]


