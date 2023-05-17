# 함수예제
# 문자열 = titlex(문자열)

# 파라미터 : 문자열
def titlex(title, msg):
    result = title
    result += ":"
    result += msg
    return result

print(titlex("시작", '환영합니다'))
print(titlex("실행", '출발하세요'))
print(titlex("종료", '귀가하세요'))

