
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    card_numbers = input().strip()         # 카드 번호 입력

    count = [0] * 10

    result = 0

    #
    # for i in range(len(Card_numbers)-1 , 0 , -1):       # 카드 정렬
    #     for j in range(i):
    #         if Card_numbers[j] > Card_numbers[j+1] :
    #             Card_numbers[j] , Card_numbers[j+1] = Card_numbers[j+1] , Card_numbers[j]

    for card in card_numbers:
        count[int(card)] += 1

    for _ in range(2):
        for idx in range(len(count)):
            if count[idx] >= 3:
                count[idx] -= 3
                result += 1

    for _ in range(2):
        for idx in range(len(count)-2):
            if count[idx] >= 1 and count[idx+1] >= 1:
                if count[idx+2] >= 1:
                    count[idx] -= 1
                    count[idx+1] -= 1
                    count[idx+2] -= 1
                    result += 1

    if result >= 2:
        baby_jin = "true"

    else:
        baby_jin = "false"

    print(f"#{test_case} {baby_jin}")







    # ///////////////////////////////////////////////////////////////////////////////////
