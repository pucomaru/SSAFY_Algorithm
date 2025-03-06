#
# import sys
# sys.stdin = open("input(15).txt", "r")

# # 중위 순회는 L -> 부모 -> R 순
def in_order(r):
    global word_put
    if r:
        in_order(left[r])
        word_put.append(word[r])
        in_order(right[r])


# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())                        # 정점의 수
    E = N - 1                               # 간선의 수

    left = [0] * (N+1)                      # 왼쪽 자식 리스트 생성
    right = [0] * (N+1)                     # 오른쪽 자식 리스트 생성
    par = [0] * (N+1)                       # 부모 리스트 생성
    word = [0] * (N+1)                      # 부모 노드에 대응하는 알파벳 넣어주기

    for i in range(N):                      # 정점 번호대로 트리 만들기
        put = input().split()
        p = int(put[0])

        word[p] = put[1]

        if len(put) >= 3:
            left[p] = int(put[2])
            par[int(put[2])] = p

        if len(put) >= 4:
            right[p] = int(put[3])
            par[int(put[3])] = p

    # 루트 찾기
    c = N
    while par[c] != 0:
        c = par[c]

    root = c

    word_put = []

    in_order(root)
    print(f"#{test_case} {''.join(word_put)}")


    # print(f"{test_case} {in_order(root)}")
# ///////////////////////////////////////////////////////////////////////////////////
