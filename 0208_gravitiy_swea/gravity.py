## 가장 큰 낙차 구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    width = int(input())                    # 가로 길이
    boxes = list(map(int,input().split()))  # 쌓여 있는 상자의 수

    max_difference = 0
    for box in boxes :

