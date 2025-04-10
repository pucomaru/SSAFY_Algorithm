
# N : 단어의 개수 
N = int(input())

# N개의 단어
words = []
for i in range(N):
    words.append(input())

# 입력받은 알파벳들 ( 중복 x)
alphabet = [] 
for word in words:
    for idx in range(len(word)):
        if word[idx] not in alphabet:
            alphabet.append(word[idx])

# 알파벳 가중치 계산
weights = {}
for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        power = length - i - 1
        weights[ch] = weights.get(ch,0) + (10 ** power)

# 가중치 기준 내림차순 정렬
sorted_weights = sorted(weights.items(), key = lambda x : x[1], reverse=True)

# 숫자 매핑 ( 큰 가중치 -> 큰 숫자)
alphabet_to_digit = {}
digit = 9
for ch, _ in sorted_weights:
    alphabet_to_digit[ch] = digit
    digit -= 1

# 단어 숫자 변환 및 합 계산
result = 0
for word in words:
    num_str = ''
    for ch in word:
        num_str += str(alphabet_to_digit[ch])
    result += int(num_str)

print(result)