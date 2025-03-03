
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M, K = map(int,input().split())      # N 사람 / M 초 / K 붕어빵 갯수
    people_come = deque(sorted(map(int, input().split())))   # 손님 도착 시간

    time = 1                                        # 초

    result = "Possible"
    #제일 늦게 오는 사람 초 까지 붕어빵 몇개까지 나오는 지 확인

    late = max(people_come)

    fish = 0

    for i in range(0,late+1):
        if i % M == 0 and i > 0:      # 초 될때마다 붕어빵 만듬 ... 누적으로 만듬
            fish += K

    # 손님 도착 시간 싹 다 보면서 손님이 받을 수 있는지 확인
        while people_come and people_come[0] == i:
            if fish > 0:
                fish -= 1
                people_come.popleft()
            else:
                result = "Impossible"
                break
        if result == "Impossible":
            break
    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
