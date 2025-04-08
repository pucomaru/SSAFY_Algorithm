
#import sys
#sys.stdin = open("input.txt", "r")

# 병합 정렬 : 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 리스트를 정렬 한 다음 , 두개 의 정렬된 부분 리스트를
# 합하여 전체가 정렬된 리스트가 되게 하는 방법

def merged(l_arr, r_arr):

    # 합쳐야 하니까 left, right 길이만큼
    result = [0] * (len(l_arr)+len(r_arr))
    l = r = 0

    # 비교할 대상이 있을때까지 반복
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] <= r_arr[r]:
            result[l+r] = l_arr[l]
            l += 1
        elif l_arr[l] > r_arr[r]:
            result[l+r] = r_arr[r]
            r += 1

    # 한쪽 리스트만 남아있을 경우 나머지 다 정렬
    while l < len(l_arr):
        result[l+r] = l_arr[l]
        l += 1

    while r < len(r_arr):
        result[l+r] = r_arr[r]
        r += 1


    return result

def merge_sorted(arr):
    global case

    if len(arr) == 1:
        return arr

    # 리스트를 반으로 나눠줌
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    #
    # print(left)
    # print(right)

    # 반으로 쪼개질 수 없을때까지 나눠줌
    left_list = merge_sorted(left)
    right_list = merge_sorted(right)

    if left_list[-1] > right_list[-1]:
        case += 1

    # 다 나눴으면 이제 합병
    merged_list = merged(left_list, right_list)

    return merged_list


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                     # N 정수의 개수
    number = list(map(int, input().split()))             # N개의 정수들

    case = 0

    sort_arr = merge_sorted(number)

    print(f"#{test_case} {sort_arr[N//2]} {case}")
    # ///////////////////////////////////////////////////////////////////////////////////
