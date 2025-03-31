# T : 체육관 개방일 수
# o, e : 여는 시간 / 닫는 시간
# N : 신청 팀 수
# Si, Fi : 시작시간 종료 시간 N개의 팀들
# 최대한 많은 팀 사용하게 하는게 목표
# -> 종료시간 빠른 순서대로 나열해가지고 빨리 끝나는 팀부터 우선순위로 하게함

# import sys
# sys.stdin = open('algo1_sample_in.txt','r')

T = int(input())

for tc in range(1, T+1):

    # 체육관 여는 시간 / 닫는 시간
    o, e = map(int, input().split())
    # 신청 팀 수
    N = int(input())
    # 신청팀들 시작시간 , 종료 시간
    apply = []
    # 신청서 받음
    for t in range(N):
        apply.append(list(map(int, input().split())))

    # 체육관 사용 가능한 팀들
    can = []
    # 체육관 영업 시간 외 신청한 팀들 제외
    for idx in range(N):
        if o <= apply[idx][0] <= e and o <= apply[idx][1] <= e:
            can.append(apply[idx])

    # 종료 시간 빠른 순서 팀 리스트
    sort_can = []
    already_sort = []

    # 종료 시간 빠른 순서대로 정렬
    while len(sort_can) < len(can):
        min_end = 24
        min_idx = 0
        for i in range(len(can)):
            if i not in already_sort and can[i][1] < min_end:
                min_end = can[i][1]
                min_idx = i
        sort_can.append(can[min_idx])
        already_sort.append(min_idx)

    # 이제 순서대로 넣어줄 거임
    match = []
    # 제일 먼저끝나는애는 미리 넣어줌
    match.append(sort_can[0])

    for idx in range(1,len(sort_can)):
        # 넣을려고 하는 팀의 시작시간이 마지막으로 들어간 팀의 종료시간보다 늦거나 같으면 체육관 이용가능
        if sort_can[idx][0] >= match[-1][1]:
            match.append(sort_can[idx])

    print(f"#{tc} {len(match)} ")