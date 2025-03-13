#import sys
#sys.stdin = open("input.txt", "r")

# 고객좌표를 싹 돌아봄. visited 이용


def dfs():


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                        # N 고객의 수
    xy = list(map(int, input().split()))     # 좌표 리스트

    firm = []
    home = []
    customer = []

    visited = [0] * len(customer)

    # 회사 좌표 / 집 좌표 추가
    firm.extend([xy[0], xy[1]])
    home.extend([xy[2], xy[3]])

    # 고객좌표 리스트 추가
    for idx in range(4,len(xy),2):
        customer.append([idx,idx+1])

    short = 1e9

    dfs()

    print(f"{test_case} {short}")




    # ///////////////////////////////////////////////////////////////////////////////////
