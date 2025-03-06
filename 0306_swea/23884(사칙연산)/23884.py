
#import sys
#sys.stdin = open("input.txt", "r")

def in_order(r):
    if r:
        in_order(left[r])
        stack.append(calculate[r])
        in_order(right[r])

# T = int(input())
# 정점이 정수면 정점 번호와 양의 정수가 주어지고
# 정점이 연산자이면
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 중위 순회로 계산

for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                                # 정점의 개수
    V = N - 1                                       # 간선

    left = [0] * (N + 1)                            # 왼쪽 자식 번호
    right = [0] * (N + 1)                           # 오른쪽 자식 번호
    parent = [0] * (N + 1)                          # 부모
    calculate = [0] * (N + 1)                       # value 들 넣음
    stack = []

    for i in range(V):
        cal = input().split()
        print (cal)
        # 연산자일 경우는 정점 번호 , 연산자 , 정점 왼쪽 자식, 정점 오른쪽 자식 받음
        if len(cal) == 4:
            p = int(cal[0])
            l_c = int(cal[2])
            r_c = int(cal[3])
            left[p] = l_c
            right[p] = r_c
            cal[p] = cal[1]
            parent[l_c] = p
            parent[r_c] = p

        # 정수일 경우는 정점 번호, 양의 정수 받음
        if len(cal) == 2:
            p= int(cal[0])
            cal[p] = cal[1]

    c = N
    while parent[c] != 0:
        c = parent[c]
    root = c

    in_order(root)

    print(calculate)






    # ///////////////////////////////////////////////////////////////////////////////////
