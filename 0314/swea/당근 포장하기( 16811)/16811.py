#import sys
#sys.stdin = open("input.txt", "r")

# N개의 당근 -> 대,중, 소로 구분하여 포장
# 같은 크기의 당근은 같은 상자
# 비어있는 상자
# 한 상자에 N//2 를 초과하면 안됨
# 앞 조건들을 만족하고 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장

from itertools import permutations

def min_difference(arr,how):
    small = 0
    medium = 0
    large = 0

    for s_idx in range(len(arr[0])):
        small += how[s_idx]

    for m_idx in range(len(arr[1])):
        medium += how[m_idx]

    for l_idx in range(len(arr[2])):
        large += how[l_idx]

    s_m = abs(small-medium)
    m_l = abs(medium-large)
    s_l = abs(small-large)

    return min(s_m, m_l, s_l)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                                # 당근의 개수
    size = list(map(int, input().split()))                          # 당근 크기
    result = 0

    # 당근 크기는 1 ~ 30
    how_many = [0] * 31

    # 당근 크기별로 몇개 있는지 정보 갱신
    for i in size:
        how_many[i] += 1

    # 한 크기의 당근이 전체 갯수의 절반 넘게 있으면 조건 만족할 수 없음 .
    for amount in how_many:
        if amount > N // 2:
            result = -1

    # 위 for 문 조건 되면 더 볼 필요가 없음
    if result == -1:
        print(f"{test_case} {result}")
        break

    # 어떤 크기의 당근들이 있는지.
    size_list = []
    for i in range(len(how_many)):
        if how_many[i] > 0:
            size_list.append(i)

    carrot_size_arrange = []
    print(size_list)
    # 소/중/대 들어갈 수 있는 숫자 경우의 수 만듬
    for s, m, l in list(map(list, permutations(size_list, 3))):
        print(list(map(list, permutations(size_list, 3))))
        print(s)
        print(m)
        print(l)
        s.sort()
        m.sort()
        l.sort()

        cant = 0
        #소/중 비교
        for i in range(len(s)):
            r = 0
            for j in range(len(m)):
                if s[i] >= m[j]:
                    r = 1
                    break
            if r == 1:
                break
        else:
            cant += 1

        #중/대 비교
        for i in range(len(m)):
            r = 0
            for j in range(len(l)):
                if s[i] >= m[j]:
                    r = 1
                    break
            if r == 1:
                break
        else:
            cant +=1

        #소/대 비교
        for i in range(len(s)):
            r = 0
            for j in range(len(l)):
                if s[i] >= m[j]:
                    r = 1
                    break
            if r == 1:
                break
        else:
            cant +=1

        if cant == 0:
            carrot_size_arrange.append([s, m, l])

    result = min_difference(carrot_size_arrange, how_many)

    print(f"{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
