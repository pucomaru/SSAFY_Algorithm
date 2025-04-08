#
# import sys
# sys.stdin = open("sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())                # 돌의 수 N / 뒤집기 횟수 M
    start = list(map(int,input().split()))                 # 초기 돌 상태
    change = [list(map(int,input().split())) for _ in range(M)]     # i 번째 돌 사이에 두고 마주보는 j개 돌 뒤집기 M번\
    # ex [[3,2],[5,3]....]

    for time in range(M):                           # 뒤집기 시작
        middle = change[time][0] - 1                # 가운데 돌 인덱스
        for i in range(1, change[time][1]+1):
            if middle - i >= 0 and middle + i <= N-1:            # 가운데 돌 왼쪽 오른쪽 값이 있을때만 뒤집기.
                if start[middle - i] == 1 and start[middle + i] == 1:
                    start[middle - i] = 0
                    start[middle + i] = 0
                elif start[middle - i] == 0 and start[middle + i] == 0: # 여기도 if 문이면 안됨. 그럼 위에서 바뀐게 여기 조건문에도 적용됨
                    start[middle - i] = 1
                    start[middle + i] = 1




    print(f"#{test_case} {' '.join(map(str,start))}")







    # ///////////////////////////////////////////////////////////////////////////////////



# T = int(input())      강사님 코드
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     stones = list(map(int, input().split()))
#
#     for _ in range(M):  # M번 반복하면서 돌 뒤집기
#         idx, spread = map(int, input().split())
#         idx -= 1    # index 는 0부터다!(헷갈린다)
#
#         for s in range(1, spread + 1):
#             left = idx - s      # 비교하려는 왼쪽 index
#             right = idx + s     # 비교하려는 오른쪽 index
#
#             # 범위 밖으로 나가면, 더 이상 안뒤집어봐도 된다.
#             if left < 0 or right >= N:
#                 break
#
#             # 양쪽이 같은 색의 돌이라면 뒤집는다.
#             if stones[left] == stones[right]:
#                 stones[left] = 1 - stones[left]
#                 stones[right] = 1 - stones[right]
#
#     print(f"#{tc}", *stones)