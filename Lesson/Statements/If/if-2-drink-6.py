# 제어문(if)

# [문제]
# 조건: 아래의 조건으로 하나만 산다.
# 돈이 5000원 이상이면 커피를 산다.
# 돈이 2000원 이상이면 사이다를 산다.
# 돈이 1000원 이상이면 생수를 산다.
# 돈이 1000원 미만이면 물을 마신다.

#money = 10000
money = 3000

# 중복되는 코드를 줄여서 하나로 기술
# 유지보수(수정) 용이
print("내가 보유하고 있는 돈:", money)

if money >= 5000:
    print("커피를 산다.")
elif money >= 2000:
    print("사이다를 산다.")    
elif money >= 1000:
    print("생수를 산다")    
else:
    print("물을 마신다.")

