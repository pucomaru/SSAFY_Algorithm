import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    sentence = input()

    stack = []

    result = 1  # 결과값

    for char in sentence:
        if char in "({":
            stack.append(char)
        if char in ")}":
            if not stack:
                result = 0
            if stack:
                top = stack.pop()
                if (char == ")" and top != "(") or (char == "}" and top != "{"):
                    result = 0

    if stack:
        result = 0



    print(f"#{test_case} {result} ")
    # ///////////////////////////////////////////////////////////////////////////////////
