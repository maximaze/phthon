# 함수
# 가변인자 : 함수의 전달되는 파라미터가 0개 이상으로 여러개가 전달
# 함수인자 앞에 아스터리스크(*)를 넣음
# 가변인자형 : 튜플(Tuple)로 전달

# 일반인자와 가변인자를 복합적으로 정의 가능
def printlist(title, *args):
    print(f"printlist: title({title}), arg({args}), type({type(args)}), len({len(args)})")
    print('arg: ', args[0])
    for a in args[0]:
        print(a)

#%%        
printlist('숫자', 1,3,5,7)
printlist('문자열', 'a','b' ,'c')
printlist('숫자문자', 'a', 1, 3,'b','c')

#%%
# [문제1] ?에 해당하는 자료형을 넣어서 함수를 호출
printlist('리스트', [2,4,6,8,10])
printlist('튜플', (1,3,5,7,9))
printlist('셋', {10,20,30,40,50})
printlist('딕셔너리', {1:'하나',2:'둘',3:'Three'})

#%%
# [문제2] 위 문제1에서 지정된 타입에 맞춰서
# 함수 printlist()에서 전달 받은 인자에서 요소를 하나씩 출력하세요.



