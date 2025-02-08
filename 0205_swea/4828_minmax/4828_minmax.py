T = int(input())

for case_num in range(1, T+1) :

    N = int(input())

    AI = list(map(int, input().split()))

    max_value = AI[0]
    min_value = AI[0]

    for idx in range(1,N):
        if AI[idx] > max_value :
            max_value = AI[idx]
        if AI[idx] < min_value :
            min_value = AI[idx]

    result = max_value - min_value

    print(f"#{case_num} {result}")


#해설


# T = int(input()) # 테스트케이스 개수
#

# for tc in range(1, T+1): # 케이스별로 처리
#     N = int(input()) # 케이스 별 입격 개수
#     arr = list(map(int, input().split()))
   

#     max_v = arr[0] # 첫 원소를 최댓값으로 가정
#     min_v = arr[0] # 첫 원소를 최솟값으로 가정
            

#     for i in range(1, N) :
#         if max_v < arr[i] : # arr[i] > max_v (다음 연산식과 비교식 순서로 맞출 것)
#             max_v = arr[i]
#         if min_v > arr[i] :
#             min_v = arr[i]

#     print(f'#{tc} {max_v-min_v}')