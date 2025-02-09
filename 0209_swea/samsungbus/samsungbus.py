
# gpt 도움 받음

import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    some_line = int(input())      # 노선 갯수
    bus_station_list = [0] * 5001 # 버스 정류장
    bus_pass=[]                   # 정류장 지나는 횟수 저장 리스트

    for i in range(some_line):  # 버스 정류장 지나 가는 노선 횟수 증가
        start, end = map(int,input().strip().split())
        for num in range(start,end+1):
            bus_station_list[num] += 1

    bus_station = int(input())

    for i in range(bus_station):
        bus_station_num = int(input())
        bus_pass.append(bus_station_list[bus_station_num])

    print(f"#{test_case} {' '.join(map(str,bus_pass))}")


    # ///////////////////////////////////////////////////////////////////////////////////
