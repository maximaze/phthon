# 정규표현식(Regular Expression)

# [문제] 정규표현식을 사용하지 않고 주민번호의 뒷자리를 '*'로 대체하라.
# 주민번호 : 123456-123567
# 화면표시 : 123456-******

data = """Park 801015-1023432
Kim 711207-2543234"""

result = []

for line in data.split('\n'):   # new line으로 나누기
    word_result = []
    for word in line.split(' '):# 공백문자로 나누기
        print('word: ', word)
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        word_result.append(word)
    
    print('word_result: ', word_result)
    result.append(' '.join(word_result))
    
print('-' * 50)
print('result: ', result)
print('-' * 50)
print('\n'.join(result))
print('-' * 50)
for rl in result:
    print(rl)

