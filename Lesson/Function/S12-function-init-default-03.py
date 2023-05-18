# 함수
# 매개변수 초기값(기본값, default value)
# 파라미터 : 전체 인자를 최기값을 지정

# 중간에 초기값을 지정하지 않고 건너 뛸 수 없다.
# SyntaxError: non-default argument follows default argument
# def move(x=1, y, z=3):

# 앞에서 초기값을 지정하고 뒤에 지정하지 않으면 안된다.
# SyntaxError: non-default argument follows default argument
# def move(x=1, y=2, z):
    
# 파라미터의 오른족 끝에서부터 초기값을 연속적으로 지정해야 한다.
def move(x,y=2,z=3):
    print('[이동]')
    print('x=', x)
    print('y=', y)
    print('z=', z)
    
#%%

# 기본값을 지정하면 파라미터를 생략 가능
# x값은 반드시 지정해야 한다. > x는 기본값이 없기 때문
move(10)        # x=10, y=2,  z=3
move(10, y=20)  # x=10, y=20, z=3
move(10, z=30)  # x=10, y=2,  z=30



