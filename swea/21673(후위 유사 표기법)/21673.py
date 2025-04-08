
import sys
sys.stdin = open("calc_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    calcultate = input()
    inside = {"+": 1, "-": 1, "*": 2, "/": 2}                      # 연산자 우선순위
    mark = []                                                       # 연산자 담을 리스트
    sentence = []
    idx = 0

    for i in calcultate:                                            # 피연산자는 바로 출력
        if i in "+-/*":
            if idx == 0:                                            # 아직 연산자 담은 리스트에 아무 것도 없으면 바로 담음
                mark.append(i)
                idx += 1
            else:
                if inside[mark[idx-1]] < inside[i]:                   # 담을 연산자가 전에 담긴 연산자보다 우선순위가 클시 담김
                    mark.append(i)
                    idx += 1                                          # 연산자 담을 리스트에 하나 추가됐으니 idx + 1
                else:
                    while inside[mark[idx-1]] >= inside[i]:           # 들어갈 연산자가 전 연산자보다 우선순위가 높을 때까지
                        mark_pop = mark.pop()                         # 전 연산자들을 빼줌
                        idx -= 1
                        sentence.append(mark_pop)
                        if idx == 0:                                  # while문 조건에서 오류나므로 break
                            break
                    mark.append(i)                                    # 다 빼줬으면 다시 연산자를 mark 에 추가

        else:                                                         # 숫자는 바로 출력
            sentence.append(i)

    for i in range(len(mark)):                                         # 문자를 다 돌았으면 축적해놓은 연산자들 차례대로 빼줌
        mark_pop = mark.pop()
        sentence.append(mark_pop)

    print(f"#{test_case} {''.join(sentence)}")
    # ///////////////////////////////////////////////////////////////////////////////////
