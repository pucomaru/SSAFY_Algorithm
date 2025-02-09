import sys
sys.stdin = open("in.txt", "r")

## 가장 큰 낙차 구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    width = int(input())                    # 가로 길이
    boxes = list(map(int,input().strip().split()))  # 쌓여 있는 상자의 수

    max_difference = 0              # 최대 낙차

    for box_index in range(width-1): # 다른 열의 상자 수 보다 많으면 낙차가 +1 마지막 박스는 다음 인덱스가 없으니 비교안함
        compare = 0                  # compare 값이 클 수록 낙차가 제일 큰 거
        for next_box_index in range(box_index+1, width):
            if boxes[box_index] > boxes[next_box_index]:
                compare += 1
        if compare>max_difference:
            max_difference = compare



    print(f"#{test_case} {max_difference}")


