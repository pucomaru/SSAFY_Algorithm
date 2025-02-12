
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    K, N, M = list(map(int,input().split()))
    # K는 최대 이동 정류장 수
    # N은 한 버스가 가는 정류장 최대 번호   0 ~ N
    # M는 충전기 설치 된 정류장 개수
    charge_bus_station = list(map(int, input().split()))      # 충전기 설치 된 정류장 번호 리스트

    now_idx = 0                                     # 출발 인덱스

    move_count = K                                  # 최대 이동 횟수

    charge_count = 0                                # 충전 횟수

    while True:                                          # 출발
        if now_idx >= N:
            break

        if move_count != 0:                         # 이동횟수가 남아있으면 이동
            move_count -= 1
            now_idx += 1

        elif move_count == 0:                       # 이동횟수가 0일 경우 ( 충전기 없는지 확인)
            if now_idx not in charge_bus_station:
                while now_idx not in charge_bus_station:    # 충전기가 없는 위치면 있을때 까지 idx 감소 있으면 while문 탈출
                    now_idx -= 1
                move_count = K                              # 충전기 있는 idx 까지 왔으니 다시 최대 이동 횟수 초기화
                charge_count += 1                           # 충전기 횟수 추가
            elif now_idx in charge_bus_station:             # 충전기 있는 idx면
                move_count = K                              # 바로 최대 이동 횟수 초기화
                charge_count += 1                           # 추

    print(f"#{test_case} {charge_count}")




    # ///////////////////////////////////////////////////////////////////////////////////
