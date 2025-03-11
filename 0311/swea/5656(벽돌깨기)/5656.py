# BFS 를 통해 깨질 벽돌들을 구하고 DFS를 통해 구슬을 쏨

from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def shoot(s, remain, now_bricks):
    global min_bricks

    # 만약 남은 벽돌이 없거나 구슬을 다 쐈으면 끝
    if s == N and remain == 0:
        if remain < min_bricks:
            min_bricks = remain
            return

    for col in range(W):
        copy_bricks = [row[:] for row in now_bricks]

        # col 위치에 구슬 떨어뜨리기
        row = -1
        for r in range(H):
            if copy_bricks[r][col]:
                row = r
                break

        if row == -1:
            continue

        q = deque([(row, col, copy_bricks[row][col])])
        now_remains = remain - 1
        copy_bricks[row][col] = 0

        while q:
            r, c, p = q.popleft()
            for k in range(1, p):
                for d in range(4):
                    ni = r + (di[d] * k)
                    nj = c + (dj[d] * k)

                    if 0 > ni or ni >= H or nj < 0 or nj >= W:
                        continue

                    if copy_bricks[ni][nj] == 0:
                        continue

                    q.append((ni, nj, copy_bricks[ni][nj]))
                    copy_bricks[ni][nj] = 0
                    now_remains -= 1

        for c in range(W):
            idx = H - 1
            for r in range(H-1, -1, -1):
                if copy_bricks[r][c]:
                    copy_bricks[r][c], copy_bricks[idx][c] = copy_bricks[idx][c], copy_bricks[r][c]

        shoot(s + 1, now_remains, copy_bricks)

import sys
sys.stdin = open("sample_input (1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, W, H = map(int,input().split())          # N 구슬 쏘는 횟수 / W 가로 / H 세로

    min_bricks = 1e9

    bricks = [list(map(int,input().split())) for _ in range(H)]

    brick = 0

    for i in range(H):
        for j in range(W):
            if bricks[i][j] != 0:
                brick += 1

    shoot(0, brick, bricks)

    print(f"#{test_case} {min_bricks}")
    # ///////////////////////////////////////////////////////////////////////////////////
