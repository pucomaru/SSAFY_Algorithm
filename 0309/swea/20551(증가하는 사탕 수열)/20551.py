# 런타임 에러남
# 사탕이 1억개가 넘으면 시간 초과 가능 성 있음
# 재귀 호출 많으면 터질 가능성 잇음
# 틀린풀이 최적화해야함 .

def eat_candy(arr):
    global eat
    global result

    if arr[0] < 1 or arr[1] < 1 or arr[2] < 1:
        return

    if arr[2] <= 2:
        return

    if arr[0] < arr[1] < arr[2] and eat == 0:
        result = 0
        return

    if arr[0] < arr[1] < arr[2]:
        result = eat
        return

    if arr[0] >= arr[1]:
        arr[0] -= 1
        eat += 1
        eat_candy(arr)

    elif arr[1] >= arr[2]:
        arr[1] -= 1
        eat += 1
        eat_candy(arr)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    candy = list(map(int, input().split()))  # 사탕 수

    eat = 0  # 먹는 횟수
    result = -1  # 결과값

    eat_candy(candy)

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////