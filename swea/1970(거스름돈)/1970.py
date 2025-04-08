
import sys
sys.stdin = open("input.txt", "r")

def change(my_money):
    change_list = [0,0,0,0,0,0,0,0]
    money_type = [50000,10000,5000,1000,500,100,50,10]

    idx = 0
    for i in money_type:
        if my_money // i >= 1:
            change_list[idx] += my_money // i
            my_money -= (my_money // i) * i
        idx += 1

    return change_list


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    money = int(input())    # 돈 입력

    print(f"#{test_case}")
    print(*change(money))

    # ///////////////////////////////////////////////////////////////////////////////////

#
    # change = [0,0,0,0,0,0,0,0] # 50000/10000/5000/1000/500/100/50/10 카운트 리스트
    #
    # if money // 50000 >= 1:
    #     change[0] += money // 50000
    #     money -= (money//50000 * 50000)
    # if money // 10000 >= 1:
    #     change[1] += money // 10000
    #     money -= (money // 10000) * 10000
    # if money // 5000 >= 1:
    #     change[2] += money // 5000
    #     money -= (money // 5000) * 5000
    # if money // 1000 >= 1:
    #     change[3] += money // 1000
    #     money -= (money // 1000) * 1000
    # if money // 500 >= 1:
    #     change[4] += money // 500
    #     money -= (money // 500) * 500
    # if money // 100 >= 1:
    #     change[5] += money // 100
    #     money -= (money // 100) * 100
    # if money // 50 >= 1:
    #     change[6] += money // 50
    #     money -= (money // 50) * 50
    # if money // 10 >= 1:
    #     change[7] += money // 10
    #     money -= (money // 10) * 10
