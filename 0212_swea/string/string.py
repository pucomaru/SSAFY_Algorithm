import sys
sys.stdin = open("test_input.txt", "r", encoding="utf-8")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    case = int(input())

    word = input().strip()  # 특정 단어
    M = len(word)  # 단어 길이

    sentence = input().strip()  # 문장
    N = len(sentence)  # 문장 길이

    word_num = 0  # 특정 단어 갯수

    i = 0
    j = 0

    while i < N:
        if sentence[i] != word[j]:
            i = i - j + 1
            j = 0

        elif sentence[i] == word[j]:
            i = i + 1
            j = j + 1
            if j == M:
                word_num += 1
                j = 0

    print(f"#{case} {word_num} ")

    # ///////////////////////////////////////////////////////////////////////////////////
