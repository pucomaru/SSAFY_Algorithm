
import sys
sys.stdin = open("4.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    number = int(input())           # 몇 개의 정수?
    numbers = list(map(int, input().strip().split()))    # 정수 리스트

    new_number_list = [0] * number                      # 특별한 정렬 리스트

    for i in range(number-1):                           # 숫자 정렬
        min_idx = i
        for j in range(i+1, number):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    for j,i in zip(range(0, len(new_number_list)-1, 2), range(len(numbers)-1, (len(numbers)//2)-1, -1)):
    # 새로운 배열 짝수 인덱스에 numbers 리스트 큰 것부터 넣기
            new_number_list[j] = numbers[i]

    for j, i in zip(range(1, len(new_number_list), 2), range(0, len(numbers)//2)):
    # 새로운 배열 홀수 인덱스에 numbers 리스트 작은 것부터 넣기
            new_number_list[j] = numbers[i]

    result=new_number_list[:10]
    # 결과 열개까지만 출력

    print(f"#{test_case} {' '.join(map(str,result))}")

    # ///////////////////////////////////////////////////////////////////////////////////
