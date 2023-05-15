# 제어문(if)
# if 조건문:
#   조건문이 참인경우 실행문
# else:
#   조건문이 참이 아닌경우 실행문    

# [비교연산자]
# 크다 : >
# 작다 : <
# 같다 : ==
# 같지 않다 : !=
# 크거나 같다 : >=
# 작거나 같다 : <=

# [논리 연산자]
# 논리합 : or
# 논리곱 : and
# 논리부정 : not

# (문제)
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어 가라.
# money = '돈이 있다'
money = '돈이 있음'

if money == '돈이 있다': # 참이면 아래 블럭을 실행
    print("택시를 타고 가라")
else: # 거짓이 이면 아리 블럭을 실행
    print("걸어 가라")    
