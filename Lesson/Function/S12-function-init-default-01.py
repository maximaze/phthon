# 함수
# 매개변수 초기값(기본값, default value)

# 파라미터 : z의 초기값은 5로 지정
# 함수 move()를 호출 할 때 z값을 지정하지 않으면 5가 지정된다.
def move(x,y,z=5):
    print('[이동]')
    print('x=', x)
    print('y=', y)
    print('z=', z)
    
#%%
move(10,20,30)  # x=10,y=20,z=30
move(10,20,z=55)# x=10,y=20,z=55

# z값을 지정하지 않고 호출
move(10,20)     # x=10,y=20,z=5
move(x=10,y=20) # x=10,y=20,z=5

#%%

# x, y값은 기본값을 지정하지 않았으므로 값을 지정해야 한다.
# TypeError: move() missing 2 required positional argument: 'x' and 'y'
# move()



