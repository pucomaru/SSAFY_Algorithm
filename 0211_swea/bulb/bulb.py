# https://www.acmicpc.net/problem/12927         강사님이 백준 풀어보라함

arr = list(input())

length = len(arr)               # 전구 갯수

count = 0                       # 스위치 누른 수 카운트

# i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.

for idx in range(length):                 # 모든 전구 상태 다 확인
    number = idx+1                          # 모든 전구 번호(number)는 idx + 1
    if arr[idx] == 'Y':                     # 전구가 Y 켜져있을때만 전구 상태 반전
        for i in range(length // number):   # 해당 전구 번호 배수 갯수 .. ex) 전구가 20개 있으면 3의 배수는 6개 있음
            if arr[idx + number * i] == 'Y':    # 현재 전구 번호 배수  3 / 3+3 / 3+3+3 /...
                arr[idx + number * i] = 'N'
            elif arr[idx + number * i] == 'N':
                arr[idx + number * i] = 'Y'
        count += 1                          # 전구를 끌때만 스위치를 누름

if 'Y' in arr:                          # 다 돌고나서도 켜져있는 전구가 있다면 -1 출력
    count = -1



print(count)
# print(arr)