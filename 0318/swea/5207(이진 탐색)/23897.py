# A 리스트 = 정렬한 상태의 리스트
# B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인
# 전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면
# 중심 원소의 인덱스 m=(l+r)//2이다.
# 이진 탐색의 왼쪽 구간은 l 부터 m-1 / 오른쪽 구간은 m+1 부터 r
# 동시 탐색 과정에서 양쪽 구간을 번걸아 선택하게 되는 숫자의 개수

import sys
sys.stdin = open("5207_input.txt", "r")

# n = 찾고자 하는 값 / l = 끝 인덱스 / r = 시작 인덱스 / move = 왼쪽 , 오른쪽 어디갔는지
def binary_search(n, l, r, m, d):
    global result

    # 들어간 인덱스 값이 찾고자 하는 값과 같거나 왼쪽오른쪽 번갈아 잘 이동했으면 result +=1
    if a_list[m] == n:
        result += 1
        return

    # 찾고자하는 값이 중간 인덱스 값 보다 클 경우
    if a_list[m] < n:
        # 전에도 오른쪽 봤는데 또 오른쪽 보면 더 볼 가치가 없음
        if d == "R":
            return
        d = "R"
        l_c = m + 1
        m_c_1 = (l_c + r) // 2
        binary_search(n, l_c, r, m_c_1, d)

    # 찾고자하는 값이 중간 인덱스 값 보다 작을 경우
    elif a_list[m] > n:
        # 전에도 왼쪽 봤는데 또 왼쪽 보면 더 볼 가치가 없음
        if d == "L":
            return
        d = "L"
        r_c = m - 1
        m_c_1 = (l + r_c) // 2
        binary_search(n, l, r_c, m_c_1, d)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int, input().split())                         # N, M : A와 B에 속한 정수의 개수
    a_list = list(map(int, input().split()))                 # a 리스트
    b_list = list(map(int, input().split()))                 # b 리스트

    a_list.sort()

    result = 0

    L = 0
    R = len(a_list)-1
    M = (L+R)//2

    for idx in range(len(b_list)):
        if b_list[idx] not in a_list:
            continue

        binary_search(b_list[idx], L, R, M, "")

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
