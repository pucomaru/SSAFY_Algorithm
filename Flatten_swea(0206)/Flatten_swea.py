
import sys
sys.stdin = open("input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    Dump_num = int(input())         # 덤프 횟수

    box = list(map(int,input().split()))    # 박스 갯수

    difference = 0 

    for i in range(Dump_num):     # 덤프 횟수 반복
        high = 0
        low = 100
        high_idx = 0
        low_idx = 0
        for idx in range(len(box)): # 제일 높은 상자 인덱스구함 / 인덱스 낮은 상자 구함     
            if box[idx] > high :
                high_idx = idx
                high = box[idx]
            if box[idx] < low :
                low_idx = idx
                low = box[idx]
        
        difference = box[high_idx] - box[low_idx]

        box[high_idx] -= 1 
        box[low_idx] += 1

        # difference = box[high_idx]-box[low_idx] # 왜 여기다 코드를 두어야하는지? 덤프를 한번 실행하고나서 차이를 구해야하는거아님??
        if difference == 1:
            break

    print(f"#{test_case} {difference}")



    # ///////////////////////////////////////////////////////////////////////////////////
