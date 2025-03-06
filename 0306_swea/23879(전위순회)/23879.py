# 전위 순회는 부모 -> L -> R 순으로 출력
#
# import sys
# sys.stdin = open("input.txt","r")

def pre_order(r):
    if r:
        print(r, end=' ')
        pre_order(left[r])
        pre_order(right[r])

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2):
    # ///////////////////////////////////////////////////////////////////////////////////
    V = int(input())                                                     # 정점의 수 V
    E = V - 1                                                            # 간선
    nums = list(map(int, input().split()))                                # 정점 번호들

    left = [0] * (V+1)                                                   # 왼쪽 자식 리스트 생성
    right = [0] * (V+1)                                                  # 오른쪽 자식 리스트 생성
    par = [0] * (V+1)                                                    # 인덱스 번호 = 자식 value = 부모

    for i in range(E):
        p, c = nums[i*2], nums[i*2+1]                                    # num 리스트 왼쪽 부모 오른쪽 자식
        if left[p] == 0:                                                 # 왼쪽 자식 넣기
            left[p] = c
        else:                                                            # 왼쪽 자식 칸이 꽉 차면 오른쪽 자식에 넣기
            right[p] = c
        par[c] = p

    c = V
    while par[c] != 0:                                               # 루트 찾기 루트는 부모 노드가 없음
        c = par[c]
    root = c
    pre_order(root)

    # ///////////////////////////////////////////////////////////////////////////////////
