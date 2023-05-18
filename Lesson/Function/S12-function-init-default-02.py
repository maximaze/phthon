# 함수
# 매개변수 초기값(기본값, default value)

# 파라미터 : 전체 인자를 최기값을 지정
def move(x=1,y=2,z=3):
    print('[이동]')
    print('x=', x)
    print('y=', y)
    print('z=', z)
    
#%%

# 기본값을 지정하면 파라미터를 생략 가능
move()          # x=1, y=2, z=3
move(y=10)      # x=1, y=20,z=3
move(z=30)      # x=1, y=2, z=30
move(10,20)     # x=10,y=20,z=3
move(x=10,z=30) # x=10,y=2, z=30
move(10,20,30)  # x=10,y=20,z=30
move(10,20,z=30)# x=10,y=20,z=30

#%%

# SyntaxError: positional argument follows keyword argument
move(x=10,88,99)
move(x=10,88,z=99)


