\
#import sys
#sys.stdin = open("input.txt", "r")

# 음식 재료 팀 짜준다음 -> 그다음 시너지 계산

def dfs(v,start,cnt):

    for idx in range(len(v)):
        v[idx] = 1
        dfs(v,start+1,cnt+1)
        v[idx] = 0

def calculate(arr):


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                                # 식재료 개수
    synergy = [map(int,input().split()) for _ in range(N)]          # 시너지

    visited =[0] * N

    dfs(visited)

    # ///////////////////////////////////////////////////////////////////////////////////
