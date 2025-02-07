import sys

sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    Dump_num = int(input())  # 덤프 횟수

    box = list(map(int, input().split()))  # 박스 갯수

    difference = 0

    for i in range(Dump_num):  # 덤프 횟수 반복
        high = box[0]
        low = box[0]
        high_idx = 0
        low_idx = 0
        for idx in range(len(box)):  # 제일 높은 상자 인덱스구함 / 인덱스 낮은 상자 구함
            if box[idx] > high:
                high_idx = idx
                high = box[idx]
            if box[idx] < low:
                low_idx = idx
                low = box[idx]

        box[high_idx] -= 1         # 덤프 해줌
        box[low_idx] += 1

        # if difference == 1:        # 차이가 1이면 더이상 진행 안해도 됨
        #    break


    high = box[0]
    low = box[0]
    high_idx = 0
    low_idx = 0

    for idx in range(len(box)):  # 제일 높은 상자 인덱스구함 / 인덱스 낮은 상자 구함
        if box[idx] > high:
            high_idx = idx
            high = box[idx]
        if box[idx] < low:
            low_idx = idx
            low = box[idx]

    difference = box[high_idx] - box[low_idx]   #덤프하고 차이 구해줌

    print(f"#{test_case} {difference}")

    # ///////////////////////////////////////////////////////////////////////////////////
