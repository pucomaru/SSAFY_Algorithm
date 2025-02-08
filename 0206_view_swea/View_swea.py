
import sys

sys.stdin = open("sample_input.txt", "r")

for Tc in range(1,11):

    T = int(input())                        # 건물 갯수 ( 양쪽 두칸 씩은 0,0) 0,0 ,.... 0,0
    N = list(map(int,input().split()))      # 건물 높이

    good_view = 0  # 조망권 좋은 세대수

    for idx in range(2, len(N)-2):
        max = 0
        if N[idx-2] > max:
            max = N[idx-2]
        if N[idx-1] > max:
            max = N[idx-1]
        if N[idx+1] > max:
            max = N[idx+1]
        if N[idx+2] > max:
            max = N[idx+2]
        if N[idx] > max:
            good_view += N[idx] - max

    print(f"#{Tc} {good_view}")

