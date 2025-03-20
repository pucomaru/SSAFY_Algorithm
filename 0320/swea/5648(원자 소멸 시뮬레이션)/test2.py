import sys
from collections import deque, defaultdict

sys.stdin = open("sample_input.txt", "r")

# 방향: 상(0), 하(1), 좌(2), 우(3)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs(atoms):
    q = deque()
    times = defaultdict(list)  # defaultdict를 사용하여 KeyError 방지
    burst = set()  # 터진 원자 저장
    max_time = 0  # 최대 시간 계산

    # 원자 초기 위치 큐에 삽입
    for idx, (x, y, d, e) in enumerate(atoms):
        q.append((x, y, d, 0, idx))  # (x, y, 방향, 시간, 원자 번호)
        times[(x, y, 0)].append(idx)  # 초기 위치 기록

    # BFS 실행
    while q:
        x, y, d, t, idx = q.popleft()

        # 터진 원자라면 이동하지 않음
        if idx in burst:
            continue

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        nt = t + 1  # 다음 시간

        # 경계를 벗어나지 않는 경우에만 이동
        if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
            times[(nx, ny, nt)].append(idx)
            q.append((nx, ny, d, nt, idx))
            max_time = max(max_time, nt)

    # 충돌 확인 (시간별 위치에 2개 이상 있는 경우)
    for t in range(max_time + 1):
        positions = defaultdict(list)
        for (x, y, time), atom_list in list(times.items()):
            if time == t:
                positions[(x, y)].extend(atom_list)

        # 같은 위치에 2개 이상의 원자가 있으면 터짐
        for atom_list in positions.values():
            if len(atom_list) > 1:
                burst.update(atom_list)  # 터진 원자 저장

    return burst


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    # 터진 원자의 집합 반환
    boom = bfs(atoms)

    # 터진 원자들의 에너지 총합 계산
    result = sum(atoms[a][3] for a in boom)

    print(f"#{test_case} {result}")
