
import sys
sys.stdin = open("sample_input.txt", "r")

# 차윤이 이동 : 앞 / 왼쪽 90도 / 오른쪽 90도
# 최소의 조작 이동 ( 최단거리 x)
# RC카는 항상 위를 바라보고있다


# 행 좌표 / 열 좌표 / 리모컨 조작 횟수 / 방향 / 나무 베는수 / field 정보
def dfs(x, y, rc, d, c, f):
    global min_control

    if rc > min_control:
        return

    if field[x][y] == "Y":
        if rc < min_control:
            min_control = rc
            return

    # G : RC카 이동 가능한 땅 / T : 나무 / Y : 도착 지점
    for z in range(4):
        nx, ny = x + direction[z][0], y + direction[z][1]

        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != "D":
            # G 이동 가능할 경우
            # 방향이 같을 경우 조작 + 1
            if field[nx][ny] == "G" and d == direction[z][2] :
                field[nx][ny] = "D"
                dfs(nx, ny, rc + 1, d, c, f)
                field[nx][ny] = "G"
            # 방향이 다를 경우
            if field[nx][ny] == "G" and d != direction[z][2]:
                # 좌/우 위/아래 짝 짝같은거끼리는 조작이 3번 다른경우는 조작이 두번
                # 짝이 같을 경우
                if direction[z][2] % 2 == d % 2:
                    field[nx][ny] = "D"
                    dfs(nx, ny, rc + 3, direction[z][2], c, f)
                    field[nx][ny] = "G"
                # 짝이 다를 경우
                else:
                    field[nx][ny] = "D"
                    dfs(nx, ny, rc + 2, direction[z][2], c, f)
                    field[nx][ny] = "G"
            # T 나무가 있을 경우
            if field[nx][ny] == "T" and d == direction[z][2] and c < cnt:
                field[nx][ny] = "."
                dfs(nx, ny, rc + 1, d, c + 1, f)
                field[nx][ny] = "T"
            if field[nx][ny] == "T" and d != direction[z][2] and c < cnt:
                if direction[z][2] % 2 == d % 2:
                    field[nx][ny] = "."
                    dfs(nx, ny, rc + 3, direction[z][2], c + 1, f)
                    field[nx][ny] = "T"
                else:
                    field[nx][ny] = "."
                    dfs(nx, ny, rc + 2, direction[z][2], c + 1, f)
                    field[nx][ny] = "T"
            # Y 도착지 일 경우
            if field[nx][ny] == "Y" and d == direction[z][2]:
                dfs(nx, ny, rc + 1, d, c, f)
            if field[nx][ny] == "Y" and d != direction[z][2]:
                if direction[z][2] % 2 == d % 2:
                    dfs(nx, ny, rc + 3, direction[z][2], c, f)
                else:
                    dfs(nx, ny, rc + 2, direction[z][2], c, f)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, cnt = map(int, input().split())               # N 필드 크기 정보 / cnt 나무 벨수 있는 카운트
    field = [list(input()) for _ in range(N)]              # 필드 정보

    # 위 0 / 좌 1 / 아래 2 / 우 3  ( 이동할때 변하는 좌표값과 방향 번호)
    direction = [(-1, 0, 0), (0, -1, 1), (1, 0, 2), (0, 1, 3)]

    # 최소 리모컨 조작 횟수 변수
    min_control = 1e9

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if field[i][j] == "X":
                dfs(i, j, 0, 0, 0, field)

    if min_control == 1e9:
        min_control = -1

    print(f"#{test_case} {min_control}")

    # ///////////////////////////////////////////////////////////////////////////////////
