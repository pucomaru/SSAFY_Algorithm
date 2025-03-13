#import sys
#sys.stdin = open("input.txt", "r")

# 고객좌표를 싹 돌아봄. visited 이용

from itertools import permutations

def distance(arr):
    global short
    d = 0

    for i in range(len(customer)-1):
        d += abs(customer[i][0] - customer[i+1][0]) + abs(customer[i][1] - customer[i+1][1])

    if d < short:
        short = d

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                        # N 고객의 수
    xy = list(map(int, input().split()))     # 좌표 리스트

    firm = []
    home = []
    customer = []

    short = 1e9

    # 회사 좌표 / 집 좌표 추가
    firm.extend([xy[0], xy[1]])
    home.extend([xy[2], xy[3]])

    # 고객좌표 리스트 추가
    for idx in range(4, len(xy), 2):
        customer.append([idx, idx+1])
    print(customer)


    orders = permutations(customer,len(customer))

    for order in orders:
        distance(order)


    print(f"#{test_case} {short}")




    # ///////////////////////////////////////////////////////////////////////////////////
