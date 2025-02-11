
import sys
sys.stdin = open("GNS_test_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    case, number_length = input().split()
    dic = {}

    dic["ZRO"] = 0                     # 행성 숫자 체계에 우리 숫자 대입
    dic["ONE"] = 1
    dic["TWO"] = 2
    dic["THR"] = 3
    dic["FOR"] = 4
    dic["FIV"] = 5
    dic["SIX"] = 6
    dic["SVN"] = 7
    dic["EGT"] = 8
    dic["NIN"] = 9

    earth = {}
    earth["0"] = "ZRO"
    earth["1"] = "ONE"
    earth["2"] = "TWO"
    earth["3"] = "THR"
    earth["4"] = "FOR"
    earth["5"] = "FIV"
    earth["6"] = "SIX"
    earth["7"] = "SVN"
    earth["8"] = "EGT"
    earth["9"] = "NIN"


    key_revert = []

    number_list = input().split()
    for i in number_list:
        key_revert.append(dic[i])

    key_revert.sort()

    key_revert = list(map(str,key_revert))

    revert_revert = []

    for i in key_revert:
        revert_revert.append(earth[i])



    print(f"{case}")
    for i in range(len(revert_revert)):
        print(revert_revert[i], end=' ')

    # ///////////////////////////////////////////////////////////////////////////////////
