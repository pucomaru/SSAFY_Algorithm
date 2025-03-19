
import sys
sys.stdin = open("5208_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    input_value = list(map(int, input().split()))
    N = input_value[0]
    battery = input_value[1:]

    now = 0
    now_battery = battery[0]
    pass_road = []
    charge = 0

    while now < len(battery):
        if now_battery > 0:
            pass_road.append((now, battery[now]))
            now += 1
            now_battery -= 1
        elif now_battery == 0:
            if now != len(battery) - 1:
                pass_road.append((now, battery[now]))
            go_idx = 0
            go_battery = -1
            for i in range(len(pass_road)):
                comparison = pass_road[i][1] - (now-pass_road[i][0])
                if comparison > go_battery:
                    go_idx = pass_road[i][0]
                    go_battery = comparison
            now = go_idx
            now_battery = battery[go_idx]
            charge += 1
            pass_road = []

    print(f"#{test_case} {charge}")
    # ///////////////////////////////////////////////////////////////////////////////////
