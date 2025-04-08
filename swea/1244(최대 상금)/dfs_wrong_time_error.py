
# import sys
# sys.stdin = open("input.txt", "r")
# 교환 모든 경우의 수 구한 다음에 최댓값 갱신
# 근데 모든 경우의 수를 다 최대값 볼려하면 타임에러뜸
# 가지를 치자 똑같은 행동을 하지말자는것
# 하다보면 ex ([1,2,3,4,5] ,2) 같이 중복되는 일이 생길텐데 check 한거를 저장해서 이미 check를 한거면 하지말자
import copy

def dfs(arr, c):
    global result
    global check

    if (tuple(arr), c) in check:
        return

    # 그냥 check.append([arr,c]) 하면 내가 원하는 값 append 안됨 .
    # 얕은 복사가 되기에 만약 arr = [1,2,3,4,5 ] 를 저장하고싶어서 check.append([[1,2,3,4,5],c]) 했는데 밑에서 arr값이 바뀌면 그 append하는 값이 바뀜
    # 왜냐 사실 append는 그 값을 저장하는게 아니라 그 리스트의 주소를 저장하는 것이기때문에 .
    check.add(arr[:], c)

    if c == change:
        num = int(''.join(map(str, arr)))
        if num > result:
            result = num
            return
        else:
            return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(arr, c + 1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, change = map(int, input().split())  # 숫자 / 교환 횟수
    number = list(map(int, str(N)))
    result = -1e9
    check = set()

    dfs(number, 0)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////