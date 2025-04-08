import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    dump = int(input())                             # 덤프 횟수
    box =list(map(int, input().split()))            # 박스 높이

    max_min = 0

    for num in range(dump):                         # 덤프를 하자
        max_box = 0                                 # 제일 높은 박스 찾기
        min_box = 101                               # 제일 낮은 박스 찾기
        max_idx = 0                                 # 제일 높은 박스 인덱스 저장
        min_idx = 0                                 # 제일 낮은 박스 인덱스 저장

        for i in range(len(box)):
            if box[i] > max_box:
                max_box = box[i]
                max_idx = i
            if box[i] < min_box:
                min_box =box[i]
                min_idx = i

        if box[max_idx] - box[min_idx] <= 1:        # 덤프 끝나기 전에 평탄화 완료하면 break
            break

        # 찾았으면 이제 덤프를 하자!!!
        box[max_idx] -= 1
        box[min_idx] += 1

    max_box = 0
    min_box = 101

    for i in range(len(box)):
        if box[i] > max_box:
            max_box = box[i]
            max_idx = i
        if box[i] < min_box:
            min_box = box[i]
            min_idx = i

    max_min = max_box - min_box

    print(f"#{test_case} {max_min}")









    # ///////////////////////////////////////////////////////////////////////////////////
