# 함수예제
# 문자열 = titlex(문자열)

# 실행이 되어야 오류를 식별할 수 있다.
# 오류가 발생하면 프로그램이 종료(멈춤)한다.

# 파라미터 : 문자열
def titlex(title, msg):
    result = title
    result += ":"
    result += msg # TypeError: can only concatenate str (not "int") to str
    return result

print(titlex("시작", '환영합니다'))
print(titlex("실행",  1234567890))    # Error
print(titlex("종료", '귀가하세요'))

# 처리결과
"""
시작:환영합니다
TypeError: can only concatenate str (not "int") to str
"""







