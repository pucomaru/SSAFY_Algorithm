
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int,input().split())             # N = 숫자 갯수 M = 맨앞 숫자 맨뒤
    numbers = list(map(int,input().split()))    # 숫자들 입력

    for i in range(M):
        num = numbers.pop(0)
        numbers.append(num)

    print(f"#{test_case} {numbers[0]}")
    # ///////////////////////////////////////////////////////////////////////////////////
