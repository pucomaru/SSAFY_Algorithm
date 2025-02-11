
# import sys
# sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    str1 = input().strip()
    str2 = input().strip()
    
    max_count = 0                           # 많은 글자 수 출력

    for i in range(len(str1)):
        count = 0                           # 카운트 수 +1
        for j in range(len(str2)):          
            if str1[i] in str2[j]:
                count += 1
        if count > max_count:
            max_count = count
    
    print(f"#{test_case} {max_count}")


    # ///////////////////////////////////////////////////////////////////////////////////
