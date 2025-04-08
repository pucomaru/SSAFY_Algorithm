# 오버핸드 셔플 / 퍼펙트 셔플
# T번의 셔플 이후 결과를 알려주는 프로그램
# 한번의 셔플 set : 오버핸드 셔플 -> 퍼펙트 셔플

from collections import deque

def overhand():
    global card
    for i in range(len(card) - (len(card) // 3)):
        left = card.popleft()
        card.append(left)
    return

def perfect():
    global card

    front = []
    back = []
    if len(card) % 2 == 0:
        for i in range(len(card) // 2):
            front.append(card[i])
            back.append(card[-1 - i])
    else:
        for i in range(len(card) // 2):
            front.append(card[i])
            back.append(card[-1 - i])
        front.append(card[len(card) // 2])

    new_arr = deque()

    if len(front) == len(back):
        for i in range(len(front)):
            new_arr.append(front[i])
            new_arr.append(back[-1-i])
    else:
        for i in range(len(back)):
            new_arr.append(front[i])
            new_arr.append(back[-1-i])
        new_arr.append(front[-1])

    card = new_arr
    return

def shuffle(cnt):
    global card
    for i in range(cnt):
        overhand()
        perfect()
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, T = map(int,input().split())                 # N 카드의 개수 / T 셔플 횟수
    card = deque(list(range(1, N+1)))
    shuffle(T)

    print(f"#{test_case} {' '.join(map(str,list(card)))}")
    print(list(card))
    # ///////////////////////////////////////////////////////////////////////////////////
