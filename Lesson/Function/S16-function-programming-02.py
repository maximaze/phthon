# Function Programming(함수형 프로그래밍)

def score(name, *args): # 외부함수
    print(f"[score] name({name}))")
    
    def minmax(func):   # 내부함수: 동적정의 // 호출될때마다 실행해서 만들어짐
        print(f"[minmax] args({args})")
        result = -1;
        for val in args:
            if result == -1:
                result = val
            result = func(result, val)    
            
        return result
    
    return minmax   # 내부함수를 리턴

#%%

s1 = score("중간시험",100,90,60,70,80)

#%%
def usermax(a,b):
    if a>=b:
        return a
    else:
        return b
 
def usermin(a,b):
    if a<b:
        return a
    else:
        return b
    
print("중간시험: 최고점수 ", s1(usermax))   # minmax(usermax)
print("중간시험: 최저점수 ", s1(usermin))   # minmax(usermin)

#%%

s2 = score("기말시험",66,77,88,99,55)
print("기말시험: 최고점수 ", s2(usermax))   # minmax(usermax)
print("기말시험: 최저점수 ", s2(usermin))   # minmax(usermin)




