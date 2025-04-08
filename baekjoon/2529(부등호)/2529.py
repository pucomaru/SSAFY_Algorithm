# 백준 2529번 부등호

def dfs(equation,idx):
    global max_num
    global min_num
    global real_min_num

    if len(equation) == k+1:
        number = "".join(map(str,equation))
        if int(number) > int(max_num):
            max_num = number
        if int(number) < int(min_num):
            min_num = number
        return


    for i in range(len(num)):
        if num[i] not in equation:
            if arr[idx] == ">" and num[i] < equation[-1]:
                equation.append(num[i])
                dfs(equation,idx+1)
                equation.pop()

            if arr[idx] == "<" and num[i] > equation[-1]:
                equation.append(num[i])
                dfs(equation,idx+1)
                equation.pop()

# k = 부등호 문자 개수
k = int(input())
# k개의 부등호들
arr = input().split()

num = [0,1,2,3,4,5,6,7,8,9]

max_num = "1"
min_num = "99999999999999"

for n in num:
    dfs([n],0)


print(max_num)
print(min_num)