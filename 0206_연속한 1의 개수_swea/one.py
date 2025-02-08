
import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    length = int(input())
    zero_one_num = input()

    total_val = 0 
    current_val = 0
    for num in zero_one_num:
        if num == '0' :
            current_val = 0
        if num == '1' : 
            current_val += 1 
            if current_val>=total_val:
                total_val = current_val 

    print(f"#{test_case} {total_val}")
    # ///////////////////////////////////////////////////////////////////////////////////
