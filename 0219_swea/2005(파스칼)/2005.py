
import sys
sys.stdin = open("input.txt", "r")

def pascal(num):

    global content

    content = [[1] for _ in range(num)]

    for i in range(1, num):
        for j in range(1, i+1):
            try:
                content[i].append(content[i-1][j-1] + content[i-1][j])
            except IndexError:
                content[i].append(1)

    return content

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())

    pascal(N)

    print(f"#{test_case}")
    for i in range(N):
        print(*content[i])
    # ///////////////////////////////////////////////////////////////////////////////////

