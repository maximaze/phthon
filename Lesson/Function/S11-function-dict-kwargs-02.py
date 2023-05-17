# 함수
# 가변인자 : dict
# 인자를 호출할 때 이름을 지정하여 호출하면 딕셔너리로 받을 수 있다.

def xyz(**kwargs):
    print(f"[xyz] type({type(kwargs)}), {kwargs}")
          
    for kw in kwargs:
        value = kwargs[kw]
        print(f"key={kw}, value={value}")
        
        
#%%

xyz(x=70, y=80,z=90)   
xyz(x=70, y=80,c=90)    




