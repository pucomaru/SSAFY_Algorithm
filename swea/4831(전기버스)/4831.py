import sys
sys.stdin = open("sample_input.txt","r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K, N, M = list(map(int,input().split()))            # K 최대 이동 정류장 수 / N번 정류장 / M 충전기 설치 정류장
    charge = list(map(int,input().split()))             # 충전기 설치된 정류장 번호
    charge_time = 0                                     # 충전 횟수
    bus = 0                                             # 버스 현재 위치
    back_count = 0                                      # 뒤로 가는 횟수
    move = K                                            # 이동

    while bus < N :
        if back_count >= K:
            charge_time = 0
            break
        if move != 0:
            bus += 1
            move -= 1
        elif move == 0 and bus in charge:
            back_count = 0
            move = K
            charge_time += 1
        elif move == 0 and bus not in charge:
            bus -= 1
            back_count += 1

    print(f"#{test_case} {charge_time}")

    # ///////////////////////////////////////////////////////////////////////////////////
