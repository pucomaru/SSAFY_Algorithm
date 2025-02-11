
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str1 = input().strip()
    str2 = input().strip()          # 공백제거 안해서 swea사이트에서 출력 오류난듯

    length_str1 = len(str1)     # str1의 길이
    length_str2 = len(str2)     # str2의 길이


    for i in range(length_str2-length_str1+1):
        if str2[i:i+length_str1] == str1:
            result = 1
            break               # 찾으면 for문 탈출 안그러면 또 돌고 reslut = 0 반환
        else:
            result = 0

    print(f"#{test_case} {result}")




    # ///////////////////////////////////////////////////////////////////////////////////
