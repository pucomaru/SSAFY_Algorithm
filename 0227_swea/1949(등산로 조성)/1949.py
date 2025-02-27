
#import sys
#sys.stdin = open("input.txt", "r")

def dfs(map):
   
    delta =[[0, 1], [1, 0], [0, -1], [-1, 0]]                       # 우 하 좌 상 (순서)

    



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                # 지도 한 변의 길이 N
    K = int(input())                # 최대 공사 가능 깊이 K

    map_information = [list(map(int,input().split())) for _ in range(N)]        # 지도 정보

    result = []                                                     # 가장 긴 등산로 길이

    dfs(map_information)


    # ///////////////////////////////////////////////////////////////////////////////////
