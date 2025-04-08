# 런타임 에러남
# 사탕이 1억개가 넘으면 시간 초과 가능성 있음

def eat_candy(arr, eats):
    global result

    # 사탕 갯수가 0이거나 두번째 상자가 1이하이거나 세번째 상자가 2이하이면 순증가 구조가 될 수 없음
    if arr[0] < 1 or arr[1] <= 1 or arr[2] <= 2:
        return

    # 먹을 필요없으면 0 리턴
    if arr[0] < arr[1] < arr[2] and eats == 0:
        result = 0
        return

    # 먹은 적 있는데 순증가 형태면 return
    if arr[0] < arr[1] < arr[2] and eats > 0:
        result = eats
        return

    if arr[0] >= arr[1]:
        eats += arr[0] - arr[1] + 1
        arr[0] = arr[1] - 1
        eat_candy(arr, eats)

    elif arr[1] >= arr[2]:
        eats += arr[1] - arr[2] + 1
        arr[1] = arr[2] - 1
        eat_candy(arr, eats)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    candy = list(map(int, input().split()))  # 사탕 수

    eat = 0  # 먹는 횟수
    result = -1  # 결과값

    eat_candy(candy, eat)

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////