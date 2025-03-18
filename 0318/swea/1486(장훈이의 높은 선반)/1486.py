
import sys
sys.stdin = open("input (7).txt", "r")

# 조합을 통해

from itertools import combinations

def check(arr):
    global able

    hap = 0
    for idxidx in range(len(arr)):
        hap += arr[idxidx]

    if hap >= B:
        able.append(hap)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, B = map(int, input().split())            # N : 점원의 수 / B: 선반 높이
    heights = list(map(int, input().split()))   # 점원의 키

    heights.sort(reverse=True)

    min_difference = 1e9

    able = []

    # 조합으로 점원들 키 팀을 만들어주고 만약 2명씩 짝을 만들어줬는데도
    # 선반 높이보다 낮으면 3명씩 팀을 만들어주는 FOR 문 ..
    # 3명 팀에서 선반 높이보다 높아지는 팀이 나오면 4명팀부터는 볼 필요가 없음

    for i in range(1, len(heights)+1):

        checkcheck = heights[:i+1]
        if sum(checkcheck) < B:
            continue

        # 중복 키 조합 방지 리스트
        do = []
        com_list = list(combinations(heights, i))
        for j in range(len(com_list)):
            if com_list[j] not in do:
                check(com_list[j])
                do.append(com_list[j])

        if len(able) > 0:
            for idx in range(len(able)):
                dif = able[idx] - B
                if dif <= min_difference:
                    min_difference = dif


    print(f"#{test_case} {min_difference}")



    # ///////////////////////////////////////////////////////////////////////////////////
