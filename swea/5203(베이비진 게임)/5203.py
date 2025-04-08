
import sys
sys.stdin = open("5203_input.txt", "r")
# 만약 숫자가 999876 이라할 경우 987 triplet 을 먼저 확인하면 999 run을 놓친다
# 그래서 run이 있나 먼저 확인하다.

def check(arr):
    visited = [0] * 10
    for i in range(len(arr)):
        visited[arr[i]] += 1

    for i in range(10):
        if visited[i] >= 3:
            return 1
    for i in range(8):
        if visited[i] >= 1 and visited[i+1] >= 1 and visited[i+2] >= 1:
            return 1
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # 카드들 (짝수 인덱스는 플레이어 1 / 홀수 인덱스는 플레이어 2)
    numbers = list(map(int, input().split()))

    player_1 = []
    player_2 = []

    winner = 0

    for idx in range(len(numbers)):
        if idx % 2 == 0:
            player_1.append(numbers[idx])
        else:
            player_2.append(numbers[idx])

        if len(player_1) >= 3:
            result = check(player_1)
            if result == 1:
                winner = 1
                break
        if len(player_2) >= 3:
            result = check(player_2)
            if result == 1:
                winner = 2
                break

    print(f"#{test_case} {winner}")
    # ///////////////////////////////////////////////////////////////////////////////////
