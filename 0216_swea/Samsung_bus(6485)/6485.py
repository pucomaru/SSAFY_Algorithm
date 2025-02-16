import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                    # 버스 노선 갯수
    bus_line = [list(map(int,input().split())) for _ in range(N)] # 버스 노선들 범위
    bus_station = int(input())                                  # 버스 정류장 갯수
    bus_stations = [int(input()) for _ in range(bus_station)]  # 버스 정류장 번호

    bus_pass_count = [0] * 5001                                       # 정류장 몇 번 지나는 지 count 하기 위해 만든 리스트
    bus_station_count = []                                            # 입력 버스 정류장 카운트 담을 리스트

    for start,end in bus_line :                                 # 지나는 횟수 등록
        for i in range(start,end+1):
            bus_pass_count[i] += 1

    for idx in bus_stations:
        bus_station_count.append(bus_pass_count[idx])





    print(f"#{test_case} {' '.join(map(str,bus_station_count))}")
    # ///////////////////////////////////////////////////////////////////////////////////
