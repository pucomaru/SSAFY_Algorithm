# 튜플로 저장한 다음 가지치기 버전

def dfs(arr, c, check):
    global result

    # 리스트를 튜플로 변환하여 저장
    if (tuple(arr), c) in check:
        return

    # 가지치기 체크
    check.add((tuple(arr), c))

    if c == change:
        num = int(''.join(map(str, arr)))
        result = max(result, num)
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(arr, c + 1, check)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for test_case in range(1, T+1):
    N, change = map(int, input().split())
    number = list(map(int, str(N)))
    result = -1e9

    dfs(number, 0, set())

    print(f"#{test_case} {result}")
