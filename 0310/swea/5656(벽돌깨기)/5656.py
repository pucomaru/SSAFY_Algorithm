# 구슬을 쏘아 벽돌을 깨뜨리는 게임
# 최대한 많은 벽돌을 깨는게 포인트!! 많은 벽돌깨고 남은 벽돌 개수 구해야함!
# 벽돌 깨면 -> 벽돌들 밑으로 떨어짐

def break():



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, W, H = map(int,input().split())          # N 공을 쏘는 횟수 / 가로 W / 세로 H
    brick = [list(map(int, input().split())) for _ in range(H)]
    copy_brick = brick

    remain_min = 999999                         # 남은 벽돌

    for shoot in range(N):
        break(copy_brick)

    print(f"{test_case} {remain_min}")
    # ///////////////////////////////////////////////////////////////////////////////////
