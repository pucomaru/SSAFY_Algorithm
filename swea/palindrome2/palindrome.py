
import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    case = int(input())

    word_space = [input() for _ in range(100)]          # 100 * 100 박스

    max_length = 0

    N = len(word_space)

    for word_length in range(1, 100):  # 회문의 길이는 1 ~ 100 ? 2, 100 결과값 이상하게 나옴
        for width in range(100):  # 행부터 돌면서 회문 찾음
            for height in range(N - word_length + 1):   # 한줄에서 몇번의 회문이 나오는 지
                result = 0
                for num in range(word_length // 2):  # 회문 한번 찾을 때마다 비교하는 횟수
                    if word_space[width][height + num] == word_space[width][height + word_length - 1 - num]:  # 반대 idx와 같다면 회문
                        result += 1
                if result == (word_length // 2):
                    now_length = word_length
                if now_length > max_length:
                    max_length = now_length

        for height in range(100):  # 열 돌면서 회문 찾음
            for width in range(N - word_length + 1):    # 한줄에서 몇번의 회문이 나오는 지
                result = 0
                for num in range(word_length // 2):  # 회문 한번 찾을 때마다 비교하는 횟수
                    if word_space[width + num][height] == word_space[width + word_length - 1 - num ][height]:  # 반대 idx와 같다면 회문
                        result += 1
                if result == (word_length // 2):
                    now_length = word_length
                if now_length > max_length:
                    max_length = now_length

    print(f"#{case} {max_length}")
    # ///////////////////////////////////////////////////////////////////////////////////
