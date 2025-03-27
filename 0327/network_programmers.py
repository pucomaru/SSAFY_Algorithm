# union-find 문제같음

# 컴퓨터 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어짐


def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union(parent, a, b):
    u_a = find_parent(parent,a)
    u_b = find_parent(parent,b)

    if a < b:
        parent[b] = u_a
    else:
        parent[a] = u_b

def solution(n, computers):
    # 연결 확인 보기 좋게
    connect = [[]for _ in range(n)]

    parent = [0] * n

    for i in range(n):
        parent[i] = i

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] ==1:
                connect[i].append(j)

    # union 합쳐줌
    for i in range(len(connect)):
        if len(connect[i]) != 0:
            for j in range(len(connect[i])):
                union(parent,i,connect[i][j])

    answer = 0

    for idx in range(n):
        if parent[idx] == idx:
            answer += 1

    return answer

# aa = solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
#
# print(aa)