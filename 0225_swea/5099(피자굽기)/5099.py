
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int,input().split())             # N은 화덕의크기 M은 피자 개수
    cheese = list(map(int, input().split()))    # 피자에 뿌려진 치즈의 양

    fire = []                                   # 화덕
    for i in range(N):                          # 초기 화덕 완성
        fire.append(cheese[i])

    rest_pizza = []                                   # 아직 안들어간 치즈들
    for i in range(N, M):
        rest_pizza.append(cheese[i])

    turn = 0                                    # 화덕 판을 돌기위해 만든 변수 0,1,... N 0,1,N...반복
    rest_idx = 0

    while 1:


    print(f"{test_case}")
    # ///////////////////////////////////////////////////////////////////////////////////
