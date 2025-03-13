N = 3
path = []

def recur(cnt, start):
    if cnt == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()

recur(0, 1)


# lambda : 재사용하지않는 함수

# 정리
# 1. 부분집합 - 비트 연산 / 2. 조합 - 재귀 호출(중복순열, 순열) / 3. 그리디 - 많이 풀어봐야 한다. ( 규칙을 못찾으면 못푼다)
