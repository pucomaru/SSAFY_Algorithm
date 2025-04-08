# kruscal 버전 -> 간선 오름차순 제일 작은 간선들 선택. 그리고 union find를 이용하여
# 안간 정점만 고르게함

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x

    else:
        parents[ref_x] = ref_y

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    parents = [i for i in range(N)]
    min_cost = 0

    # 간선들 모두 저장
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((x_list[i] - x_list[j]) ** 2 +
                    (y_list[i] - y_list[j]) ** 2) * tax
            edges.append((i, j, cost))

    # 2. 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 3. 싸이클을 검사하면서, 앞에서부터 간선을 연결한다.
    # - 언제까지 반복 ? N-1 개의 간선이 선택될 때 까지
    count = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            min_cost += w
            count += 1
            if count == N - 1:
                break

    print(f"#{tc} {min_cost:.0f}")