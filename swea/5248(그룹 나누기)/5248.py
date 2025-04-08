
import sys
sys.stdin = open("sample_input.txt", "r")

def find_set(x):
    if leader[x] != x:
        leader[x] = find_set(leader[x])
    return leader[x]

def union(x,y):
    global leader

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x != ref_y:
        leader[ref_y] = ref_x

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int, input().split())                  # N 출석 번호 / M 신청서
    arr = list(map(int, input().split()))             # 신청서

    leader = [i for i in range(N+1)]

    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])

    groups = set()
    for i in range(1,N+1):
        groups.add(find_set(i))

    print(f"#{test_case} {len(groups)}")

    # ///////////////////////////////////////////////////////////////////////////////////
