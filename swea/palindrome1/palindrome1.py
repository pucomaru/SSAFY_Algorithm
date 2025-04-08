
#import sys
#sys.stdin = open("input.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    word_length = int(input())                      # 찾아야 하는 회문의 길이
    word_space = [input().strip().split() for _ in range(8)]        # 8 * 8 글자판 생성

    N = len(word_space)                             # 글자판 길이

    count = 0                                       # 회문 카운트

    for width in range(8):                          # 행부터 돌면서 회문 찾음
        for height in range(8):
            for i in range(N-word_length+1):        # 한 줄에서 몇번 회문을 찾는지 
                result = False
                for num in range(word_length//2):             # 회문 한번 찾을 때마다 비교하는 횟수
                    if word_space[width][height + i + num] == word_space[width][height + word_length - 1 - num + i]:        # 반대 idx와 같다면 회문
                        result = True                   
                    if word_space[width][height + i + num] != word_space[width][height + word_length - 1 - num + i]:        # 반대 idx와 다르다면 회문 x
                        result = False
                if result == True:
                    count += 1
                
    for height in range(8):                          # 열열 돌면서 회문 찾음
        for width in range(8):
            for i in range(N-word_length+1):        # 한 줄에서 몇번 회문을 찾는지 
                result = False
                for num in range(word_length//2):             # 회문 한번 찾을 때마다 비교하는 횟수
                    if word_space[width + i + num][height] == word_space[width + word_length - 1 - num + i][height]:        # 반대 idx와 같다면 회문
                        result = True                   
                    if word_space[width + i + num][height] != word_space[width+ word_length - 1 - num + i][height]:        # 반대 idx와 다르다면 회문 x
                        result = False
                if result == True:
                    count += 1    

    print(f"#{test_case} {count}")

        


    # ///////////////////////////////////////////////////////////////////////////////////
