# 제어문(if)

# [문제]
# 조건: 아래의 조건으로 하나만 산다.
# 돈이 5000원 이상이면 커피를 산다.
# 돈이 2000원 이상이면 사이다를 산다.
# 돈이 1000원 이상이면 생수를 산다.
# 돈이 1000원 미만이면 물을 마신다.

money = 10000

if money >= 5000:
    print("내가 가지고 있는 돈:", money)
    print("커피를 산다.")
elif money >= 2000: # else if
    print("내가 가지고 있는 돈:", money)
    print("사이다를 산다.")    
elif money >= 1000:
    print("내가 가지고 있는 돈:", money)
    print("생수를 산다")    
else:
    print("내가 가지고 있는 돈:", money)
    print("물을 마신다.")

