
#import sys
#sys.stdin = open("input.txt", "r")

def forth(co):

    stack = []                                    # 피연산자 담을 스택

    result = "error"                              # 에러값
    error =
    for char in co:
        if char not in "+-*/" and char != '.':    # 피연산자일 경우 스택에 담음
            stack.append(int(char))

        else:                                     # 연산자일 경우 스택에서 정수를 꺼내 계산해야함
            if char == '.':                       # . 만나면 스택에 있는 숫자를 꺼내야함
                if len(stack) == 1 and type(stack[0]) == int:   # 스택에는 정수 하나만 들어가야함
                    return stack[0]
                else:
                    return result

            if len(stack) <= 1:                   # char == '.' 이 아닌데 stack에 한개가 들어있으면 오류
                return result

            else:
                a = stack.pop()                   # 스택 뒤 두 정수를 가져와 계산
                b = stack.pop()

                if char == "+":
                    stack.append(a + b)
                if char == "-":
                    stack.append(b - a)
                if char == "*":
                    stack.append(int(a * b))      # 무조건 int형 문제읽
                if char == "/":
                    stack.append(int(b / a))
                if char == "%":
                    stack.append(b % a)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    code = input().split()

    print(f"#{test_case} {forth(code)}")
    # ///////////////////////////////////////////////////////////////////////////////////
