# 백준 14888 (연산자 끼워넣기)

# 수열 , 연산자 주어짐 이들을 조합해서 계산된 결과의 최댓값 , 최소값 구하기

def calculate(arr):
    result = []
    for i in range(len(arr)):


def dfs(idx,op,cal):

    if len(cal) == N+N-1:
        calculate(cal)
        return
    
    # 숫자 계산식에다 넣기기
    cal.append(numbers[idx])

    for i in range(len(op)):
        if op[i] >= 1:
            cal.append(op[i])
            op[i] -= 1
            dfs(idx+1,op,cal)
            cal.pop()
            op[i] +=1


# N 수의 개수
N = int(input())

# 숫자들 
numbers = list(map(int,input().split()))

# 연산자 개수 ( + , -, *, / )  -> 개수 합하면 N-1개
operator_num = list(map(int,input().split()))

min_sum = 1e9
max_sum = -1 

# 숫자 idx, 연산자 개수, 식 담을 리스트 
dfs(0,operator_num,[])

