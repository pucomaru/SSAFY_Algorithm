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
    # 터진 원자들
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

            q.append((nx, ny, d, nt, idx))

    # q에 든게 없으면 이제 이동할 수 있는 원자가 없는거
    # 이제 충돌 확인을 해준다
    # times 딕셔너리 형태인데 만약에 time[(1000,5,3)] = [ 1, 2]
    # 면 3초에 1000,5 위치에 원자 1,2가 있다는것임 따라서
    # value 길이가 2이상인것들은 당연히 터지는거
    # 터지는 원자들을 burst 에 담아 줄 것인데 왜 set로 지정했냐면
    # 내 코드는 원자들이 만나면 터지고 그뒤로 사라지는게 아니라 일단 끝까지 가게 지정을 짰으므로
    # 터져야할 원자가 안터지고 쭉 가다가 다른 원자를 또 만나서 터질 수 있기에
    # 중복을 처리하기위해 set를 이용함
    for value in times.values():
        if len(value) >= 2:
            for i in value:
                if i not in burst:
                    burst.add(i)
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
