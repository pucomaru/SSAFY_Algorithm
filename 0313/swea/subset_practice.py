# 1. 이터툴즈 사용
# 2. math 사용
# 3. 부분집합 비트로 이용
# ---------------------------------------------------------------------------
#첫번째 케이스 (이터툴즈 사용)
from itertools import combinations

friends = ['A', 'B', 'C', 'D', 'E']

case = 0

for i in range(2, len(friends)):
    f = list(combinations(friends, i))
    case += len(f)


print(case)

# ---------------------------------------------------------------------------

# 두번째 케이스 ( math 사용 )
import math

friends = ["a", 'b', 'c', 'd', 'e']

cnt = 0
for i in range(2, len(friends)):
    cnt += math.comb(len(friends), i)

print(cnt)


# ---------------------------------------------------------------------------
#세번째 케이스 (뷰분집합 비트연산 사용)

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# 1 인 bit 수를 반환하는 함수
def get_count(tar):
    count = 0
    for i in range(n):
        if tar & 0x1:
            count += 1
            tar >>= 1
        return count

# 모든 부분 집합 중 원소의 수가 2개 이상이 집합의 수
answer = 0
# 모든 부분집합을 확인
for target in range(1 << n):
    # 만약, 원소의 개수가 2개 이상이면 answer += 1
    if get_count(target) >= 2:
        answer += 1

print(answer)
