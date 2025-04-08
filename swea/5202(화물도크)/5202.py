
import sys
sys.stdin = open("sample_input(4).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                                                        # 신청서 N
    application = [list(map(int, input().split())) for _ in range(N)]       # 작업 시작 / 종료 시간

    # 종료시간을 기준으로 정렬
    application.sort(key=lambda x: (x[1]))

    # ok된 신청서들
    # 일단 종료시간 제일 빠른건 옮길 수 있어서 추가함
    can = [application[0]]

    # 최근에 ok된 신청시간 종료시간과 지금 확인하는 신청서 시작시간이랑 비교하고 종료시간보다 같거나 크면 화물 작업 ok
    for i in range(1, len(application)):
        if application[i][0] >= can[-1][1]:
            can.append(application[i])

    print(f"#{test_case} {len(can)}")




    # ///////////////////////////////////////////////////////////////////////////////////
