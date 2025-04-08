## dfs 버전

def synergy(arr):                           # 시너지 계산 (음식 짝 지어준거 매개변수로 받음)
    food_synergy = 0
    for i in range(len(arr)-1):             # j는 i+1 부턴데 i를 len(arr)로 하면 인덱스 오류남
        for j in range(i+1,len(arr)):
            food_synergy += food[arr[i]][arr[j]] + food[arr[j]][arr[i]]
    return food_synergy

def dfs(k, i):                                  # k는 음식 재료 선택 개수 / i는 음식재료 idx
    global minimum

    if k == N//2 :                              # 음식 재료 N//2 선택했으면 시너지계산 나머지 N//2는 알아서 따라옴
        food_a = []
        food_b = []
        for i in range(N):                      # visited 돌면서 값이 1인 것들은 a 리스트에 추가
            if visited[i] == 1:
                food_a.append(i)
            else:                               # 아닌것들은 알아서 b 리스트에 추가
                food_b.append(i)

        a = synergy(food_a)                     # a 리스트 , b 리스트 시너지 합들 구하고 차이 구함
        b = synergy(food_b)
        minimum = min(minimum, abs(a-b))
        return
    #
    for idx in range(i,N):                      # ex ) 음식 재료 0,1,2,3 있으면 처음엔 visited가 [0,0,0,0]
        if not visited[idx]:                    # 음식 재료 0은 visited[0] = 0 을 visited[0] 로 바꿔줌
            visited[idx] = 1                    # 음식재료 0을 선택했으니 다음 재료 선택으로 넘어감
            dfs(k+1, idx+1)                     # dfs(1, 1) 로 넘어가서 또 1을 선택하게된다면 4개중에 두개를 선택했으니 위에 if 문걸려서 시너지 계싼

            visited[idx] = 0                    # 백트래킹
                                                # 선택말고 안선택했을 경우도 있으니 다시 0으로 돌려줌

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                    # 식재료 개수

    food = [list(map(int,input().split())) for _ in range(N)]             # 음식 시너지
    visited = [0] * N       # visited 를 이용해 음식 재료 짝 지어줌 .

    minimum = 999999

    dfs(0, 0)       # 음식 재료 선택 수 / 인덱스 전달

    print(f"#{test_case} {minimum}")
    # ///////////////////////////////////////////////////////////////////////////////////




