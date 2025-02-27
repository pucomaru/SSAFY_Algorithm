
from itertools import permutations

def calculate_num(num_arr):
    num_sum = 0

    

    while 1:
        if len(num_arr) == 1:
            break
        elif len(num_arr) >= 3:
            if num_arr[1] == "+":
                num_sum = num_arr[0] + num_arr[2]

            elif calculate[1] == "-":
                num_sum = num_arr[0] - num_arr[2]

            elif calculate[1] == "*":
                num_sum = num_arr[0] * num_arr[2]

            elif calculate[1] == "/":
                num_sum = int(num_arr[0] / num_arr[2])

            num_arr[0] = num_sum
            num_arr.pop(1)
            num_arr.pop(1)

    num_sum = num_arr[0]
    return num_sum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                                   # N개의 숫자
    operator_num = list(map(int,input().split()))                      # 연산자 갯수 + = * /
    numbers = list(map(int,input().split()))

    operator = ["+","-","*","/"]
    use_operator = []                                                  # 사용하는 연산자 담을 리스트

    idx = 0                                                            # 연산자 인덱스

    max_result = -1e9                                                  # 계산 최댓값
    min_result = 1e9                                                   # 계산 최소값

    # 계산에 쓸 연산자 리스트 만들어준다.
    for num in operator_num:
        if num == 0:
            pass
        else:
            for i in range(num):
                use_operator.append(operator[idx])
        idx += 1

    # 연산자 리스트 순서 모든 경우의 수를 구한 리스트 만들어줌  . ( 1,2,3,4), (1,2,4,3).... (4,3,2,1)

    arr = []
    for i in range(len(use_operator)):
        arr.append(i+1)

    num_permutations = list(permutations(arr))      # 연산자 순서 모든 경우의 수
    # 모든 경우의 수를 구한 리스트 내부를 모두 돌면서 숫자와 연산자를 조합해 계산을 해주며 최대값과 최소 값을 구함 .
    # 연산자 순서대로 스택에 담아줌 . 이제 계산할 때 문자 스택에 하나 . 연산자 스택에 하나씩 꺼내면서 계산 queue이용 선입선출
    for number in num_permutations:
        calculate = []                              # 계산식 담음
        stack_op = []                               # 연산자 담을 스택
        cal_result = 0                              # 계산 결과
        for i in number:
            stack_op.append(use_operator[i-1])        # 스택에 연산자 순서대로 담음
        for i in range(N + len(use_operator)):      # 계산식 만듬
            if i % 2 == 0:
                calculate.append(numbers[i//2])
            else:
                calculate.append(stack_op[i//2])
                
        # 이제 계산식 리스트에서 하나하나씩 꺼내서 계산을 해주자
        result = calculate_num(calculate)

        if max_result < result :                    # 계산 최댓값 갱신
            max_result = result
        if min_result > result:                     # 계산 최솟값 갱신
            min_result = result

    difference = max_result - min_result

    print(f"#{test_case} {difference} ")
    # ///////////////////////////////////////////////////////////////////////////////////
