

# 아이디어 : 모든 칸을 돌면서 그 칸이 갈 수 있는 모든 경로의 값을 dfs로 구해준다.
# 꼭 사각형 형태로 돌아야함 => 모든 방향을 한번씩 다 써야함 . 만약에

def dfs(species, first_spe, now, go):                   # 디저트 종류 2차원 배열 / 첫번째 디저트 종류 /첫 시작 인덱스 / 대각선 방향
    # 처음 인덱스와 이동한 인덱스가 같으면 dfs 문 탈출
    first = now                                         # 현재 인덱스는 계속 바뀔 예정이므로 첫번째 인덱스 저정해줌

    if now == first:
        result.append()

    if now[0]






T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                              # 한 변의 길이
    dessert = [list(map(int,input().split())) for _ in range(N)]  # 디저트 종류

    delta = [[-1, -1], [1, -1], [-1, 1], [1, 1]]                  # 왼쪽 위 / 왼쪽 아래 / 오른쪽 아래 / 오른쪽 위

    for i in range(N):                                            # 모든 칸을 돌면서 최대 디저트 경로를 구해줌
        for j in range(N):
            now_idx = [i,j]                                       # 첫 시작 인덱스
            first_species = dessert[i,j]                          # 첫 시작 디저트종류
            dfs(dessert, first_species , now_idx, delta)

    result = []                                                   # 모든 경로 값을 추가함

    print(f"{test_case} {max(result)}")
    # ///////////////////////////////////////////////////////////////////////////////////
