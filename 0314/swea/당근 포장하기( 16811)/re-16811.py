#import sys
#sys.stdin = open("input.txt", "r")

# N개의 당근 -> 대,중, 소로 구분하여 포장
# 같은 크기의 당근은 같은 상자
# 비어있는 상자
# 한 상자에 N//2 를 초과하면 안됨
# 앞 조건들을 만족하고 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장

def dfs(s, e):
    global small
    global middle
    global large
    global result

    small = []
    middle = []
    large = []

    if s == e:
       return

    for i in range(s):
        small.append(size_arr[i])
    for j in range(s, e):
        middle.append(size_arr[j])
    for k in range(e, len(size_arr)):
        large.append(size_arr[k])

    s_hap = 0
    m_hap = 0
    l_hap = 0

    for idx in small:
        s_hap += size_arr[idx]
    for idx in middle:
        m_hap += size_arr[idx]
    for idx in large:
        l_hap += size_arr[idx]

    max_hap = max(s_hap, m_hap, l_hap)
    min_hap = min(s_hap, m_hap, l_hap)

    difference = max_hap - min_hap

    if difference < result:
        result = difference

    dfs(s+1, e-1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                # 당근의 개수
    size = list(map(int, input().split()))                          # 당근 크기
    result = 1e9

    # 당근 크기는 1 ~ 30
    how_many = [0] * 31

    # 당근 크기별로 몇개 있는지 정보 갱신
    for i in size:
        how_many[i] += 1

    size_arr = []

    for i in range(len(how_many)):
        if how_many[i] > 0:
            size_arr.append(i)

    dfs(1, len(size_arr)-1)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
