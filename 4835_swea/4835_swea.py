
import sys
sys.stdin = open("4835_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N , M = map(int,input().split()) # 정수의 개수 N 구간의 개수 M

    num = list(map(int,input().split())) # N개의 정수 ai

    num_sum= 0

    sum_list=[]

    for i in range(N-M+1):
        num_sum = sum(num[i:i+M])
        sum_list.append(num_sum)

    max_number = sum_list[0] 
    min_number = sum_list[0]

    for i in range(1,len(sum_list)):
        if sum_list[i] > max_number :
            max_number = sum_list[i]
        if sum_list[i] < min_number :
            min_number = sum_list[i]

    result = max_number-min_number

    print(f"#{test_case} {result}")


    # ///////////////////////////////////////////////////////////////////////////////////
