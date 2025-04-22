# N개의 구역
# 구역은 1 ~ N번까지 번호가 매겨짐
# 구역은 두 개의 선거구로 나눠야함
# 각 구역은 두 선거구 중 하나에 포함
# 선거구는 구역을 적어도 하나 포함, 한 선거구에 포함되어있는 구역은 모두 연결

# 두 선거구에 포함된 인구의 차이를 최소로 하는 것이 문제

from itertools import combinations

def

# 구역 개수
N = int(input())

# 구역에 속한 인구 수
sector_people = list(map(int, input().split()))

# 각 구역들과 인접한 구역의 정보 ( 인덱스 0: 인접한 구역의 수 / 그 뒤 인덱스들은 이제 인접 구역 번호 )
adj_sector = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    sector_div = list(combinations(range(1, N+1), i))
    a_sector = []
    b_sector = []
    for idx in range(len(sector_div)):
        a_sector = sector_div[idx]
        b_sector = list(set(range(1, N+1))-set(a_sector))




