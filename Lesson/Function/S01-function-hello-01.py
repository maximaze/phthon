# 함수(Function)
# 함수는 호출하기 전에 정의가 되어 있어야 한다.
# 함수의 리턴값이 없는 경우 리턴값을 받으면 None이다.
# 함수 정의에서 리턴값이 없으면 return을 생략하면 된다.
# 함수 정의에서 파라미터가 없으면 함수() 형태로 파라미터를 생략한다.
"""
함수정의

def 함수명(파라미터):
    명령문
    return 리턴값
"""
#%%

# 함수가 정의되기 전에 함수를 호출하면?
# NameError : name 'hello' is not defined
# hello()

#%%



# 함수정의
# 파라미터 : 없음
# 리턴값 : 없음
def hello():
    print("Hello, World")
    
# 함수 호출
hello()

# 함수가 리턴값이 없을 경우 리턴값을 출력하려고 하면?
print(hello()) # None

# 함수가 리턴값이 없을 경우 리턴값을 변수에 받으려 하면?
msg = hello()
print("msg : ", msg)










