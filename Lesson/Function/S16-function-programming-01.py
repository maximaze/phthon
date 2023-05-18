# Function Programming(함수형 프로그래밍)

def score(name, *args): # 외부함수
    print(f"[score] name({name}))")
    
    def minmax():   # 내부함수: 최소값, 최대값
        min = -1;
        max = -1;
        for val in args:
            if min == -1 or val < min:
                min = val
            
            if max == -1 or val > max:
                max = val
                
        return min, max
    return minmax   # 내부함수를 리턴

#%%
# 독립객체로 보기 때문에 따로 클래스를 만들지 않아도 값을 중복적용됨
s1 = score("중간시험",100,90,60,70,80)
s2 = score("기말시험",88,88,77,66,55,44)

print("중간시험(최소값, 최대값): ", s1())   # 내부함수를 실행
print("기말시험(최소값, 최대값): ", s2())   # 내부함수를 실행

print("중간시험(최소값, 최대값): ", s1())   # 내부함수를 실행
print("기말시험(최소값, 최대값): ", s2())   # 내부함수를 실행