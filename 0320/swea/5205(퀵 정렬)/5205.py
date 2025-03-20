
import sys
sys.stdin = open("sample_input(3).txt", "r")

# 피벗 : 제일 왼쪽 요소
def hoare_partition(left, right):
    pivot = number[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and number[i] <= pivot:
            i += 1
        while i <= j and number[j] >= pivot:
                j -= 1
        if i < j:
            number[i], number[j] = number[j], number[i]

    number[left], number[j] = number[j], number[left]
    return j

def quick_sort(left,right):
    if left < right:
        pivot = hoare_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = intinput())                                # N 정수의 개수

    number = list(map(int,input().split()))         # 숫자들

    quick_sort(0, len(number) - 1)

    print(f"#{test_case} {number[N//2]}")

    # ///////////////////////////////////////////////////////////////////////////////////
