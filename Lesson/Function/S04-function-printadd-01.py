# 함수
# 매개 변수를 지정하여 호출하기

def printadd(title,x,y):
    print(f"[{title}]")
    print(f" x : {x}")
    print(f" y : {y}")
    print(f"---------")
    print(f" + : {x+y}")
    
#%%

# 함수호출
# 인자는 순서대로 전달
# title : '숫자덧셈'
# x : 10
# y : 20
printadd('숫자 덧셈', 10,20)

#%%
# 매개 변수를 지정하여 호출하기
# 함수의 정의된 파라미터의 이름을 지정하여 호출

printadd(x=90, y=80, title='매개 변수를 지정하여 호출')
printadd(y=90, x=80, title='매개 변수를 지정하여 호출')

#%%
# 함수의 매개 변수 일부만 이름을 지정하여 호출
# 매개변수의 처음부터 순서를 맞추고 뒤에 오는 매개변수를 이름을 지정 가능
printadd('문자열덧셈', x="안녕", y="반갑습니다")
printadd('문자열덧셈', y="Hi", x="안녕")
printadd('문자열덧셈', "Hello", y="World.")


#%%
# // x값이 정해지지 않았기에  y값이 먼저오면 순서가 꼬여서 오류가 나오는듯함
# // 값이 명시적으로 나오지 않는한 순서가 맞게 먹어야함
# 함수의 매개 변수를 일부만 지정할 때 순서를 섞으며 안된다.
# SyntaxError: positional argument follows keyword argument
printadd('문자열덧셈', y="World.", "Hello" )
printadd(x="안녕", y="반갑습니다", '문자열덧셈')



