# greedy로 했는데 예외 경우의수가 더 많아서 틀림

#import sys
#sys.stdin = open("input.txt", "r")
# 앞 숫자판부터 제일 높은 숫자로 교체해줌

def dfs(arr, start_i, c):
    global result

    # 교환 횟수를 다 썼거나 비교 인덱스가 마지막 인덱스면 더 할 가치가 없음
    if c == change or start_i == len(number) - 1:
        num = int(''.join(map(str, arr)))
        if num > result:
            result = num
            return

    # 제일 큰 수 , idx 저장
    max_num = [arr[start_i], start_i]

    for i in range(start_i + 1, len(number)):
        if arr[i] > max_num[0]:
            max_num = [arr[i], i]

    if max_num[1] == start_i:
        dfs(arr, start_i + 1, c)

    else:
        arr[start_i], arr[max_num[1]] = arr[max_num[1]], arr[start_i]
        dfs(arr, start_i + 1, c + 1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, change = map(int, input().split())   # 숫자 / 교환 횟수
    number = list(map(int, str(N)))
    result = -1e9

    dfs(number, 0, 0)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
