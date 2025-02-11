

'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    case = int(input())

    N = 100

    ladder = [list(map(int, input().strip().split())) for _ in range(N)]            # 스도쿠 생성

    result_idx = 0

    start_point = []

    for height in range(100):
            if ladder[0][height] == 1:
                
                while True:
                    if ladder[width][height-1] != 1 and ladder[width][height+1] != 1: # 오른쪽 길이랑 왼쪽 길이 없으면 행 밑으로
    
                    if ladder[width][height+1] == 1:        # 오른쪽 길이 있으면 오른쪽으로
                        while ladder[width][height] != 0:
                            height += 1                     # 왼쪽 길이 있으면 왼쪽으로
    
                    if ladder[width][height-1] == 1 :
                        while ladder[width][height] != 0:
                            height -= 1
    
                    if width == 99:
                        if ladder[width][height] == 2:
                            result_idx == height
    
                    width += 1
    
                    if width == 100:
                        break

    print(f"{case} {result_idx}")

    # ///////////////////////////////////////////////////////////////////////////////////
