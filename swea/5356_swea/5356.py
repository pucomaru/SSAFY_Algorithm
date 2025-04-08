# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    case = 5                # 단어는 5개

    blackboard =[[" "] * 15 for _ in range(case)]          # 칠판 크기 ( 각 줄 길이는 1이상 15이하)

    for i in range(case):
        word = input().strip()                     # 의석이가 쓴 단어
        for j in range(len(word)):
            blackboard[i][j] = word[j]             # 의석이가 쓴 단어 칠판에 붙임
        # print(word)


    read_words = []                                # 의석이가 쓴 단어 세로방향으로 읽은 거 저장

    # print(blackboard)

    for height in range(len(blackboard[0])):
        for width in range(case):
            if blackboard[width][height] != ' ':
                read_words.append(blackboard[width][height])

    # print(read_words)         왜 blackboard 6열 부분이 저장안됨?

    print(f"#{test_case} {''.join(map(str,read_words))} ")
    # ///////////////////////////////////////////////////////////////////////////////////




# 라이브 강사님이 품 

# A = 'ABCD'
# B  = 'EFGHIJKLMN'

# N = len(A)
# M = len(B)
# i = j = 0           #A[i], B[j]
# ans = ''
# while i+j < N+M:
#     if i < N:
#         ans += A[i]
#         i += 1
#     if j < M:
#         ans += B[i]
#         j += 1
# prin(ans)
# ans = [0] * (N+M):
# while i+j < N+M:
#     if i < N:
#         ans[i+j] = A[i]
#         i += 1
#     if j < M:
#         ans[i+j] = B[j]
#         j += 1
# print(j.)