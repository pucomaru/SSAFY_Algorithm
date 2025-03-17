from copy import deepcopy

def change_2(arr):
    global change_b2
    for i in range(len(arr)):
        copy_arr = list(arr)
        if copy_arr[i] == '0':
            copy_arr[i] = '1'
        elif copy_arr[i] == '1':
            copy_arr[i] = '0'
        change_b2.append("".join(copy_arr))

def change_3(arr):
    global change_b3
    for i in range(len(arr)):
        arr = list(arr)
        copy_arr = deepcopy(arr)
        if copy_arr[i] == '2':
            copy_arr[i] = '1'
            change_b3.append("".join(copy_arr))
            copy_arr[i] = '0'
            change_b3.append("".join(copy_arr))

        elif copy_arr[i] == '1':
            copy_arr[i] = '2'
            change_b3.append("".join(copy_arr))
            copy_arr[i] = '0'
            change_b3.append("".join(copy_arr))

        elif copy_arr[i] == '0':
            copy_arr[i] = '1'
            change_b3.append("".join(copy_arr))
            copy_arr[i] = '2'
            change_b3.append("".join(copy_arr))

def cal_2(arr):
    num_sum = 0
    reverse_arr = arr[::-1]
    for i in range(len(reverse_arr)):
        if int(reverse_arr[i]) == 1:
            num_sum += 2 ** i
    return num_sum

def cal_3(arr):
    num_sum = 0
    reverse_arr = arr[::-1]

    for i in range(len(reverse_arr)):
        if reverse_arr[i] != 0:
            num_sum += int(reverse_arr[i]) * (3 ** i)
    return num_sum


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    bin_2 = input()
    bin_3 = input()

    change_b2 = []
    change_b3 = []

    change_2(bin_2)
    change_3(bin_3)

    result = 0

    for a in range(len(change_b2)):
        for b in range(len(change_b3)):
            if cal_2(change_b2[a]) == cal_3(change_b3[b]):
                result = cal_2(change_b2[a])
                break
        if result:
            break


    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
