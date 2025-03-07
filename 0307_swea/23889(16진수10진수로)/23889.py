
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 16진수 문자 1차 배열 주어진 거 7 bit 씩 묶어 십진수로 변환
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    arr = input().split()                           # 16진수 문자

    change = []

    order = 0
    # 배열을 7개씩 묶어줌 1~7 글자 한팀 8~14 글자 두번째 팀
    for i in range((len(arr) // 7) + 1):
        try:
            change.append(arr[order:order+7])
            order += 7

        except IndexError:
            # 인덱스 오류나는 부분은 arr 마지막 팀에서 오류남
            idx = len(arr) - (len(arr) // 7 * 7)
            rest = []
            while idx >= len(arr):
                rest.append(arr[idx])
                idx += 1
            change.append(rest)






    print(f"{test_case}")
    # ///////////////////////////////////////////////////////////////////////////////////
