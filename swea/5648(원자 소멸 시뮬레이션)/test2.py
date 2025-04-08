import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

# 방향: 상(0), 하(1), 좌(2), 우(3)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs(atom):
    q = deque()
    times = {}  # 초당 원자 위치 저장
    burst = set()  # 터진 원자 저장

    # 원자 초기 위치 큐에 삽입
    for idx, (x, y, d, e) in enumerate(atom):
        q.append((x, y, d, 0, idx))

    while q:
        x, y, d, t, idx = q.popleft()

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        nt = t + 1  # 다음 시간

        # 경계를 벗어나지 않는 경우에만 이동
        if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
            if (nx, ny, nt) not in times:
                times[(nx, ny, nt)] = [idx]
            else:
                times[(nx, ny, nt)].append(idx)

                # **즉시 터지는 원자 감지!**
                if len(times[(nx, ny, nt)]) >= 2:
                    burst.update(times[(nx, ny, nt)])

            # **터진 원자는 큐에 추가하지 않음**
            if idx not in burst:
                q.append((nx, ny, d, nt, idx))

    return burst


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    boom = bfs(atoms)

    result = sum(atoms[a][3] for a in boom)  # 터진 원자의 에너지를 합산

    print(f"#{test_case} {result}")
