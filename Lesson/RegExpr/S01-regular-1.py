# 정규표현식(Regular Expression)

# [문제] 정규표현식을 사용하지 않고 주민번호의 뒷자리를 '*'로 대체하라.
# 주민번호 : 123456-123567
# 화면표시 : 123456-******

data = """Park 801015-1023432
Kim 711207-2543234"""

result = []

for line in data.split('\n'):
    word_result = []
    for word in line.split(' '):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        word_result.append(word)
    
    result.append(' '.join(word_result))
    
print('result: ', result)




