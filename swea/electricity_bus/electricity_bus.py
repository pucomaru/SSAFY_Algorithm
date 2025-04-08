
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    K, N, M = list(map(int,input().strip().split()))
    # K는 최대 이동 정류장 수
    # N은 한 버스가 가는 정류장 최대 번호   0 ~ N
    # M는 충전기 설치 된 정류장 개수
    charge_bus_station = list(map(int, input().strip().split()))      # 충전기 설치 된 정류장 번호 리스트
    # print(charge_bus_station)
    now_idx = 0                                     # 출발 인덱스
    move_count = K                                  # 최대 이동 횟수
    charge_count = 0                                # 충전 횟수
    # back_count = 0                                  # 뒤로 간 횟수

    while now_idx < N:                                          # 출발
        back_count = 0 
        # back_count = 0 
        if move_count != 0:                         # 이동 횟수가 남아 있으면 이동
            move_count -= 1
            now_idx += 1

        elif move_count == 0:                       # 이동 횟수가 0일 경우 ( 충전기 없는지 확인)
            if now_idx not in charge_bus_station:
                while now_idx not in charge_bus_station:    # 충전기가 없는 위치면 있을때 까지 idx 감소 있으면 while문 탈출
                    now_idx -= 1
                    back_count += 1
                if back_count >= K:                         # 뒤로 가는 걸 최대 이동 횟수 만큼 하면 앞으로 나아갈 수가 없음
                    charge_count = 0
                    break
                move_count = K                              # 충전기 있는 idx 까지 왔으니 다시 최대 이동 횟수 초기화
                charge_count += 1                           # 충전 횟수 추가
            elif now_idx in charge_bus_station:             # 충전기 있는 idx면
                move_count = K                              # 바로 최대 이동 횟수 초기화
                charge_count += 1                           # 충전 횟수 추가

    print(f"#{test_case} {charge_count}")




    # ///////////////////////////////////////////////////////////////////////////////////
