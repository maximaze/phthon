# 함수예제
# 문자열 = titlex(문자열)

# 실행이 되어야 오류를 식별할 수 있다.
# 오류가 발생하면 프로그램이 종료(멈춤)한다.

# 파라미터 : 문자열
def titlex(title, msg):
    if isinstance(title,str) != True:
        return f"함수의 파라미터 title({title})값이 문자열이 아닙니다."
    
    if isinstance(msg,str) != True:
        return f"함수의 파라미터 msg({msg})값이 문자열이 아닙니다."
    
    result = title
    result += ":"
    result += msg
    return result

print(titlex("시작", '환영합니다'))
print(titlex("실행", 1234567890))
print(titlex(1234567890, '출발하세요'))
print(titlex("종료", '귀가하세요'))

# 처리결과
"""
시작:환영합니다
실행:1234567890
종료:귀가하세요
"""

def titlex(A,B):
    result = int(A)
    result += A
    result += "+"
    result += int(B)
    result += B
    result += "="
    result += A+B
    return result

print(titlex("1", "2"))








