T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T + 1):
    A, B = input().strip().split()  # A와 B 입력 받기

    idx = 0
    count = 0

    while idx < len(A):
        if A[idx:idx + len(B)] == B:  # B를 찾으면
            count += 1
            idx += len(B)  # B의 길이만큼 점프
        else:
            count += 1
            idx += 1  # 그냥 한 글자 입력

    print(f"#{test_case} {count}")
