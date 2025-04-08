
import sys
sys.stdin = open("input.txt", "r")

def mirror(char):
    if char == 'b':
        return 'd'
    if char == 'd':
        return 'b'
    if char == 'p':
        return 'q'
    if char == 'q':
        return 'p'



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    input_string = list(input().strip())
    length = len(input_string)

    reverse_input_string = input_string[::-1]


    for idx in range(length):
        reverse_input_string[idx] = mirror(reverse_input_string[idx])

    print(f"#{test_case} {''.join(reverse_input_string)}")

    # ///////////////////////////////////////////////////////////////////////////////////
