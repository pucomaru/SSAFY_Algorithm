N = int(input())                                             # 구역 N 개
people = list(map(int,input().split()))                      # 각 구역 인구 수

adj_list = [[] * N]

for i in range(N):
    info = list(map(int,input().split()))               # 인접한 구역의 수 / 인접한 구역의 번호

    for j in range(info[0]):                            # 인접 리스트 생성
        idx = 1
        adj_list[i].append(info[idx])
        idx += 1


# 구역으 두개의 선거구로 나눠야함
A_zone = []
B_zone = []

