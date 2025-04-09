def dfs(num)
# N : 단어의 개수 
N = int(input())

word_1 = input()
word_2 = input()

visited = [0] * 10

alphabet = [] 
for w in word_1:
    if w not in alphabet:
        alphabet.append(w)

for w in word_2:
    if w not in alphabet:
        alphabet.append(w)

number = [9,8,7,6,5,4,3,2,1,0]
use_alphabet = number[:len(alphabet)]

num_dic = {}
