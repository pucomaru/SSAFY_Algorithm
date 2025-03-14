#import sys
#sys.stdin = open("input.txt", "r")

# N개의 당근 -> 대,중, 소로 구분하여 포장
# 같은 크기의 당근은 같은 상자
# 비어있는 상자
# 한 상자에 N//2 를 초과하면 안됨
# 앞 조건들을 만족하고 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장

def dfs(s, m, l, v):

    




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                # 당근의 개수
    size = list(map(int, input().split()))                          # 당근 크기
    result = 0

    small = []
    middle = []
    large = []

    # 당근 크기는 1 ~ 30
    how_many = [0] * 31

    # 당근 크기별로 몇개 있는지 정보 갱신
    for i in size:
        how_many[i] += 1

    print(how_many)

    dfs(small, middle, large, how_many)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
