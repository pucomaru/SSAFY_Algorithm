
import sys
sys.stdin = open("sample_input.txt", "r")

def transport(container,trucks,container_length,truck_count):
    total_weight = 0                # 옮긴 화물 전체 무게

    container_weight_rank = []
    truck_weight_rank = []
    max_container = 0

    for i in range(container_length):                 # 컨테이너 무게 큰 순서대로 나열
        for con in container:
            if con > max_container :
                max_container = con
        container_weight_rank.append(max_container)
        container.remove(max_container)
        max_container = 0

    count = 1                                       # 트럭 수 만큼 실을 수 있는 화물 무게 계싼
    for one in container_weight_rank:               # 컨테이너 무게 나열한 순대로 트럭에 담을 수 있는지 비교
        for truck in trucks:
            if one <= truck:
                total_weight += one
                trucks.remove(truck)
                count += 1
                break
        if count > truck_count:
            break

    return total_weight







T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N , M = map(int,input().split())    # 컨테이너 수 N / 트럭 수 M
    container_weight = list(map(int,input().split()))       # N개 화물 무개
    truck_amount = list(map(int,input().split()))           # M개 트럭 적재용량

    print(f"#{test_case} {transport(container_weight, truck_amount, N , M)}")
    # ///////////////////////////////////////////////////////////////////////////////////
