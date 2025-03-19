
import sys
sys.stdin = open("sample_input.txt", "r")



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int, input().split())                  # N 출석 번호 / M 신청서
    arr = list(map(int, input().split()))             # 신청서

    team = 0

    leader = [0] * (N + 1)

    for i in range(len(leader)):
        leader[i] = i

    for i in range(0, len(arr), 2):
        leader[arr[i+1]] = arr[i]

    for i in range(1, len(leader)):
        if leader[i] == i:
            team += 1

    print(f"#{test_case} {team}")

    # ///////////////////////////////////////////////////////////////////////////////////
