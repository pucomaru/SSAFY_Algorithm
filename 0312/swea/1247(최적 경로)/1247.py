
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                # 고객의 수
    xy = list(map(int,input().split()))             # 좌표들

    firm = []                                       # 회사 좌표
    home = []                                       # 집 좌표
    customer = []

    # 회사 좌표
    firm.append(xy[0], xy[1])
    home.append(xy[2], xy[3])

    # ///////////////////////////////////////////////////////////////////////////////////
