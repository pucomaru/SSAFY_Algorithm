
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    honey_sum = 0

    N, M, C = map(int,input().split())                  # N: 벌통들의 크기 / M: 선택할 수 있는 벌통의 개수 / C: 꿀을 채취할 수 있는 최대 양

    honey = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):                                  # 첫번째 양봉업자 최대 합 인덱스 구하기
        for j in range(N-1):



    for i in range(N):                                  # 두번째 양봉업자 최대 합 인덱스 구하기
        for j in range(N-1):


    print(f"{test_case} {honey_sum}")
    # ///////////////////////////////////////////////////////////////////////////////////
