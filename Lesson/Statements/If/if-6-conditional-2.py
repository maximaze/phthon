# 제어문(if)
# 조건부 표현식(conditional expression)
# 결과 = 참 if 조건식 else 거짓
#   - 조건식이 만족하면 참의 값을 결과에 리턴
#   - 조건식이 만족하지 않으면 거짓의 값을 결과에 리턴

# score = 70
score = 59
succ = None

if score >= 60:
    succ = "합격"
else:
    succ = "불합격"    

print('succ=', succ)

# 위의 문장을 아래의 문장으로 변환
# 조건부 표현식(conditional expression)
msg = "합격" if score >= 60 else "불합격"

print('msg=', msg)    

# 자바(Java)
# msg = (score >= 60) ? "합격" : "불합격";