import sys
sys.stdin = open("sample_input.txt", "r")

for Tc in range(1,11):

    N = int(input())                # 건물의 개수
    buildings = list(map(int, input().split()))     # 건물들 높이

    light = 0

    for i in range(2, N-2):
        compare =  [-1, -2, 1, 2]                           # 현재 인덱스를 기준으로 양쪽 건물 확인
        now_light = 255
        for num in compare:
            if buildings[i] - buildings[i+num] <= 0:        # 지금 빌딩보다 큰 빌딩이 있으면 비교할 필요가 없음. 조망권 확보 0
                now_light = 0
                break
            else:
                if buildings[i] - buildings[i + num] < now_light:
                    now_light = buildings[i] - buildings[i + num]
        light += now_light

    print(f"#{Tc} {light}")



