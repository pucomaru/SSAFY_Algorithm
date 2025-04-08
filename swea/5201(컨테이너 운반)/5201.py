
import sys
sys.stdin = open("sample_input(3).txt", "r")

# 그리디
# 최대 많은 용량 옮기는게 목적 그럼 제일 무거운 거부터 옮길 수 있는 지 확인.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())                     # N 컨테이너 수 / M 트럭 수
    container = list(map(int, input().split()))      # 컨테이너들 화물 무게
    truck = list(map(int, input().split()))          # 트럭 적재용량

    # 옮길 화물 무게들
    truck.sort(reverse=True)
    move = []
    for t in truck:
        heavy = 0
        heavy_idx = 0
        for idx in range(len(container)):
            # 제일 무겁고 트럭에 담을 수 있는 한번도 옮긴 적 없는 컨테이너
            if idx not in move and container[idx] > heavy and t >= container[idx]:
                heavy = container[idx]
                heavy_idx = idx
        if heavy > 0:
            move.append(heavy_idx)

    weight = 0
    for idx in move:
        weight += container[idx]

    print(f"#{test_case} {weight}")




    # ///////////////////////////////////////////////////////////////////////////////////
