
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    card_num = int(input())                     # N개의 카드
    card_name = input().split()

    forth = []                                   # 앞부분 인덱스 카드 이름 넣기
    back = []                                    # 뒷부눈 인덱스 카드 이름 넣기

    if card_num % 2 == 0:
        for idx in range(card_num//2):
            forth.append(card_name[idx])

        for idx in range(card_num//2, card_num):
            back.append((card_name[idx]))
    else:
        for idx in range(card_num // 2 + 1):
            forth.append(card_name[idx])

        for idx in range(card_num // 2 + 1, card_num):
            back.append((card_name[idx]))

    new_list = []
    if card_num % 2 == 0:
        for i in range(len(forth)):
            new_list.append(forth[i])
            new_list.append(back[i])
    else:
        for i in range(len(back)):
            new_list.append(forth[i])
            new_list.append(back[i])
        new_list.append(forth[card_num // 2])

    print(f"#{test_case} {' '.join(new_list)}")
    # ///////////////////////////////////////////////////////////////////////////////////
