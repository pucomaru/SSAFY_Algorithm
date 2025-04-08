
#import sys
#sys.stdin = open("input.txt", "r")

# 트리의 일부 = 서브 트리
# 서브트리에 속한 노드 개수 -> 루트 기준이므로 후위 순회때
def post_order(r):
    global cnt

    if r:
        post_order(left[r])
        post_order(right[r])
        cnt += 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # 간선 E, 루트 N
    E, root = map(int, input().split())
    N = E + 1           # 정점
    # 부모, 왼쪽 자식, 오른쪽 자식
    parent, left, right = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

    # 부모 자식 노드 번호쌍
    node_num = list(map(int, input().split()))
    for i in range(E):
        p = i * 2
        c = i * 2 + 1

        if left[node_num[p]] == 0:
            left[node_num[p]] = node_num[c]
        else:
            right[node_num[p]] = node_num[c]

    cnt = 0

    post_order(root)

    print(f"#{test_case} {cnt}")

    # ///////////////////////////////////////////////////////////////////////////////////
