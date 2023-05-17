# 함수 예제
# 가변 인자를 활용한 예제

# [문제] multiavg() 함수를 완성하세요.
# args : 가변인자로 여러개의 숫자가 전달
# return : 가변인자로 전달된 총합의 평균을 구함

#내가 한거
def multiavg(*args):
    for a in args[:]:
        print(len(args),"개 값의 평균")
        sum = 0
        for a in args[:]:
            sum += a
            print(f"a={a}, sum={sum}")
        return sum/int(len(args))

    
#%%
#강사님께서 하신거
 def multiavg(*args):
    total = 0
    
    for x in args:
        total += x
    return total / len(args)
#%%
s1 = multiavg(1,2,3,4,5)    # 평균
s2 = multiavg(70,80,90,100) # 평균

print('s1= ', s1)
print('s2= ', s2)