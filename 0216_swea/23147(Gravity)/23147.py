
import sys
sys.stdin = open("in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    max_fall = 0                # 가장 큰 낙차

    width = int(input())                          # 가로 길이
    box = list(map(int, input().split()))         # 쌓여 있는 상자의 수


    for i in range(width):          # i는 첫번째 박스
        count = 0                   # 낙차 세기
        j = 0
        while i+j < width:
            if box[i] > box[i+j]:
                count += 1
            j += 1
        if count > max_fall:
            max_fall = count


    print(f"#{test_case} {max_fall} ")
    # ///////////////////////////////////////////////////////////////////////////////////
