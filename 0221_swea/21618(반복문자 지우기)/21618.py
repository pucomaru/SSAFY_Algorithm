
#import sys
#sys.stdin = open("input.txt", "r")
#

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    strings = input()                        # 문자열 입력

    stack = []                               # 스택에 중복되지않은 문자만 담게됨

    for char in strings:
        if stack and stack[-1] == char:      # 중복되는 문자가 담겨도 알아서 이 조건문에서 빠짐
            stack.pop()
        else:
            stack.append(char)


    print(f"#{test_case} {len(stack)}")
    # ///////////////////////////////////////////////////////////////////////////////////
