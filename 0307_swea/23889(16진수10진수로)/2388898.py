T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 16진수 문자 1차 배열 주어진 거 7 bit 씩 묶어 십진수로 변환
# -> 일단 2진수로 다 변환한 후 7 bit 단위로 나누자
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    hex_num = input()  # 16진수 문자

    # 16진수 -> 10 진수 -> 2진수
    # 2부터 슬라이싱 한 이유는 앞에 2진수를 표기해주는 문자를 빼기위해
    bin_num = bin(int(hex_num, 16))[2:]

    # 7 bit 로 나눈것들 넣을 리스트
    change = []

    # idx 시작 변수
    order = 0

    # 2진수 7bit씩 묶는 반복문
    for i in range((len(bin_num) // 7) + 1):
        try:
            change.append(bin_num[order:order + 7])
            order += 7

        except IndexError:
            # 인덱스 오류나는 부분은 arr 마지막 팀에서 오류남
            idx = len(bin_num) - (len(bin_num) // 7 * 7)
            rest = []
            while idx >= len(bin_num):
                rest.append(bin_num[idx])
                idx += 1
            change.append(rest)

    real_change = [0]
    # 묶은 것들 다시 10진수로
    for bins in change:
        real_change.append(int(bins, 2))

    print(f"#{test_case} {' '.join(map(str,real_change))}")
    # ///////////////////////////////////////////////////////////////////////////////////
