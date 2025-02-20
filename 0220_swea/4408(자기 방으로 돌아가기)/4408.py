
import sys


#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                    # 돌아가야 할 학생들의 수

    # 현재 방 / 돌아가야 할 방

    return_list = [[] for _ in range(N)]

    for i in range(N):
        now_room, return_room = map(int, input().split())
        return_list[i].append(now_room)
        return_list[i].append(return_room)

    print(return_list)


    # ///////////////////////////////////////////////////////////////////////////////////
