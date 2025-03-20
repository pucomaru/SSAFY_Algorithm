import sys
sys.stdin = open("sample_input.txt", "r")

# bfs 를 이용
# 초당 원자 이동 .. 1초 원자이동 쫙 .. 2초 원자이동 쫙...
# 이렇게 초당 원자 이동을 기록할 것이기때문에 bfs를 이용할 것임

from collections import deque

# 방향 상 하 좌 우
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(atom):

    q = deque()
    # 초당 원자 위치 담을 딕셔너리
    times = {}
    # 터진 원자들 중복방지를 위해 집합
    burst = set()

    # 원자 시작 위치 쫙 q에 담아줌
    for idx, (x , y, d, e) in enumerate(atom):
        # 좌표, 방향, 시간초, 원자 idx 저장
        q.append((x, y, d, 0, idx))

    while q:
        # 위치 , 방향 , 시간, 원자 번호
        x, y, d, t, idx = q.popleft()
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        nt = t + 1

        # 경계를 벗어나면 안됨
        if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
            # times 딕셔너리에 초랑 위치 담아줄거임
            if (nx, ny, nt) not in times:
                times[(nx, ny, nt)] = [idx]
            else:
                times[(nx, ny, nt)].append(idx)

                # ex ) ( 100, 50, 3 ) 가 2 이상이라는것은 3초에 좌표 100,50 에 있는가 원자가 2이상이라는 뜻이므로 터짐
                # 따라서 터지는 idx들을 burst 집합에 넣어줘야함.
                if len(times[(nx, ny, nt)]) >= 2:
                    burst.update(times[(nx, ny, nt)])

            # burst 에 idx가 있으면 이미 터진 원자이므로 q에 append 할 필요가 없음
            if idx not in burst:
                q.append((nx, ny, d, nt, idx))

    return burst

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # N 원자들의 수
    N = int(input())

    # 원자들의 x 위치 (0) , y 위치 (1) , 이동 방향 (2), 보유 에너지 k (3)
    atoms = [list(map(int, input().split())) for _ in range(N)]

    boom = bfs(atoms)

    result = 0

    # 터진 원자들 에너지 다 더 해줌
    for a in boom:
        result += atoms[a][3]

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
