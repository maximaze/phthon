# 함수
# 가변인자 : dict

def xyz(**kwargs):
    print(f"[xyz] type({type(kwargs)}), {kwargs}")
    print("x=", kwargs['x'])
    print("y=", kwargs['y'])
    print("z=", kwargs['z'])

#%%

# 인자의 전달: {'x':70, 'y':80, 'z':90}
xyz(x=70, y=80,z=90)    
    
#%%

# 함수를 호출할 때 인자의 이름을 지정하지 않으면?
# TypeError: xyz() takes 0 positional arguments but 3 were given
xyz(70,80,90)   # 오류발생
    
#dict
# TypeError: xyz() takes 0 positional arguments but 1 was given
# 파라미터를 1개로 인식 // {}요거 딕트 먹인걸 하나로 올려서인듯
xyz({'x':70, 'y':80, 'z':90}) # 오류발생

#%%
# 각각의 인자로 자료형이 dict
xyz(x={'x':70}, y={'y':80}, z={'z':90})

#%%
# 함수가 인지할 수 없는 파라미터를 전달하면 오류
xyz(x=70, y=80, z=90)



