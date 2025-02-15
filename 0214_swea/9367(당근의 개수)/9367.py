
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////



    carrot = int(input())                   # 당근의 갯수
    carrot_size = list(map(int, input().split()))
    max_num = 1  # 연속 커지는 횟수 최대 길이0
    len_sum = 1  # 연속 커지는 횟수

    for i in range(carrot-1):
        if carrot_size[i] < carrot_size[i+1]:
            len_sum += 1
        else:
            if len_sum > max_num :
                max_num = len_sum
            len_sum = 1

    max_num = max(max_num, len_sum)



    print(f"#{test_case} {max_num}")
    # ///////////////////////////////////////////////////////////////////////////////////
