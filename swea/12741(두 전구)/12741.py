
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # 전구 X 켜져있던 시간 A~B / 전구 Y 켜져 있던 시간 C~D
    A, B, C, D = map(int, input().split())
    together = 0

    set1 = set(range(A, B))
    set2 = set(range(C, D))

    set3 = set1 & set2


    print(f"#{test_case} {len(set3)}")
    # ///////////////////////////////////////////////////////////////////////////////////
