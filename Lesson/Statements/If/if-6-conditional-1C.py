# 제어문(if)
# 조건부 표현식(conditional expression)

# score = 70
score = 50
message = "불합격"

if score >= 60: # 60이상이면
    message = "합격"

# 변수가 선언되어 있지 않으면 None 체크 되지 않음
# NameError: name 'message' is not defined
'''
if message != none:
    print(message)
'''

print(message)    
