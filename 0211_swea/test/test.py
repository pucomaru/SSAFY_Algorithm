# 강사님이 백준 https://www.acmicpc.net/problem/12927 문제 냄 
# https://www.acmicpc.net/problem/12927




arr = list(input())             # 전구 Y/N 리스트 입력받음 

length = len(arr)               # 전구 갯수

count = 0                       # 스위치 누른 수 카운트

for idx in range(length):                 # 모든 전구 상태 다 확인
    number = idx+1                          # 모든 전구 번호(number)는 idx + 1
    if arr[idx] == 'Y':                     # 전구가 Y 켜져있을때만 전구 상태 반전
        for i in range(length // number):   # 해당 전구 번후 배수 갯수
            if arr[idx + number * i] == 'Y':
                arr[idx + number * i] = 'N'
            elif arr[idx + number * i] == 'N':
                arr[idx + number * i] = 'Y'
        count += 1

if 'Y' in arr:                          # 다 돌고나서도 켜져있는 전구가 있다면 -1 출력
    count = -1



print(count)
# print(arr)