
import sys
sys.stdin = open("5247_input.txt", "r")

from collections import deque

def bfs(n):
    global result

    q = deque()
    q.append(n)

    while q:
        value = q.popleft()

        if 1 <= value <= 1000000:

            if value == M:
                result = visited[value]
                return

            if visited[value - 1] == 0:
                q.append(value - 1)
                visited[value - 1] = visited[value] + 1
            if visited[value - 10] == 0:
                q.append(value - 10)
                visited[value - 10] = visited[value] + 1
            if (0 < value + 1 <= 1000000) and visited[value + 1] == 0:
                q.append(value + 1)
                visited[value + 1] = visited[value] + 1
            if (0 < value * 2 <= 1000000) and visited[value * 2] == 0:
                q.append(value * 2)
                visited[value * 2] = visited[value] + 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M = map(int, input().split())                 # N = 자연수 / M = 만들어야 하는 자연수

    visited = [0] * 1000001

    result = -1

    bfs(N)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
