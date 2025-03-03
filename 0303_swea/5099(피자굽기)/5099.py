#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):

    N, M = map(int,input().split())         # N 화덕의 크기 / M 피자 개수
    cheese = list(map(int,input().split())) # M개의 피자에 뿌려진 치즈양

    fire = []                                # 화로
    rest = deque()                       # 못 들어간 피자
    melt = []                               # 녹은 순서대로 피자 번호 리스트에 삽입

    # 화로에 넣을 수 있는 만큼 피자 넣음  (치즈양 정보, 몇번째 피자인지)
    for i in range(N):
        fire.append([cheese[i], i])

    # 남은 피자 (치즈양 정보, 몇번째 피자인지)
    for i in range(N,M):
        rest.append([cheese[i], i])

    while 1:
        if len(melt) == M:                  # 피자가 다 녹으면 중지
            break

        # 화로 한번 녹일때마다 치즈 양 반 줄어둠
        for i in range(N):
            if fire[i][0] == -1:            # -1 은 빈칸이라는 뜻 빈칸 일때는 다음 칸으로 넘어감 .
                continue

            fire[i][0] //= 2                # 빈칸이 아니면 녹임

        for i in range(N):
            if fire[i][0] == 0 and rest :   # 치즈가 다 녹았고 넣을 피자가 있을 경우
                melt.append(fire[i][1])
                fire[i] = rest.popleft()

            elif fire[i][0] == 0 and not rest : # 치즈가 다 녹았는데 넣을 피자가 없을 경우
                melt.append(fire[i][1])
                fire[i][0] = -1

    print(f"#{test_case} {melt[M-1]+1}")
    # ///////////////////////////////////////////////////////////////////////////////////
