


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    word = input()
    check = 0

    check_cnt = 0
    for i in range(len(word)//2):
        if word[i] == word[len(word) - i - 1]:
            check_cnt += 1

    if check_cnt == len(word) // 2 :
        check = 1

    print(f"#{test_case} {check}")

    # ///////////////////////////////////////////////////////////////////////////////////
