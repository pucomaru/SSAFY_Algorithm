import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque
# dfs 와 bfs 활용
# dfs 로 원자 하나하나 최대 깊이 까지 간 다음
# bfs 로 초당 같은 거리에 있는 원자들 찾은 다음 에너지 계산.

def dfs(loc, direction, t, i):
    # 상 (y만 +) ( y가 1000 이하여야함)
    if direction == 0 and loc[1] <= 1000:
        dfs([loc[0], loc[1] + 1], direction, t+1, i)
        times[t+1].append(loc[0], loc[1] + 1, i)

    # 하 (y만 -) ( y가 -1000 이상이여야함)
    elif direction == 1 and loc[1] >= -1000:
        dfs([loc[0], loc[1] - 1], direction, t+1, i)
        times[t+1].append(loc[0], loc[1] - 1, i)

    # 좌 (x만 -) ( x가 -1000 이상이여야함)
    elif direction == 2 and loc[0] >= -1000:
        dfs([loc[0] - 1, loc[1]], direction, t+1, i)
        times[t+1].append(loc[0] - 1, loc[1], i)

    # 우 (x만 +) ( x가 1000 이하여야함
    elif direction == 3 and loc[0] <= 1000:
        dfs([loc[0] + 1, loc[1]], direction, t+1, i)
        times[t+1].append(loc[0] + 1, loc[1], i)

def check(t, energy):

    # t초에 있는 움직인 원자가 없으면 더 이상 볼필요가 없음
    if len(times[t]) == 0:
        return

    now_time = []
    now_atom = []

    for atom in times[t]:
        if [atom[0], atom[1]] not in now_time:
            now_time.append(atom[0], atom[1])
            now_atom.append(atom[2])
        elif [atom[0], atom[1]] in now_time:
            burst.add(atom[3])
            jungbok_idx = now_time.index([atom[0], atom[1]])
            burst.add(jungbok_idx)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # N 원자들의 수
    N = int(input())

    # 원자들의 x 위치 (0) , y 위치 (1) , 이동 방향 (2), 보유 에너지 k (3)
    atoms = [list(map(int, input().split())) for _ in range(N)]

    # 초당 어떤 원자들이 있는지 담을 리스트 n초에 [x좌표,y좌표,원자번호]가 담길 것임
    times = [0] * 2001

    # 터진 원자
    burst = set()

    # dfs로 원자 하나하나 초당 어디에 있는 지 그래프 만들어줌
    for idx in range(N):
        # 현재 위치 , 방향, 몇초, 몇번쨰 원자인지 변수로 줌
        dfs([atoms[idx][0], atoms[idx][1]], atoms[idx][2], 0, idx)

    check(1, 0)

    print(f"{test_case} {len(burst)}")

    # ///////////////////////////////////////////////////////////////////////////////////
