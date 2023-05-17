# 함수
# 가변인자 : 함수의 전달되는 파라미터가 0개 이상으로 여러개가 전달
# 함수인자 앞에 아스터리스크(*)를 넣음
# 가변인자형 : 튜플(Tuple)로 전달

# 일반인자와 가변인자를 복합적으로 정의 가능
def printlist(title, *args):
    print(f"printlist: title({title}), arg({args}), type({type(args)}), len({len(args)})")
    
    for px in args:
        print(f"2번째 인자: [{px}] type({type(px)})")
        if isinstance(px, dict): # 딕셔너리
            print("<dict>")
            ks = list(px.keys())
            for k in ks:
                print(f"key[{k}],value[{px[k]}]")
            print("-" * 50)
            dl = list(px.items())
            for item in dl:
                print(f"key[{item[0]}],value[{item[1]}]")
        elif isinstance(px, list): # 리스트
            print("<list>")
            for v in px:
                print(f"value[{v}]")
        elif isinstance(px, set): # 셋
            print("<set>")
            for v in px:
                print(f"value[{v}]")
        elif isinstance(px, tuple): # 튜플
            print("<tuple>")
            for v in px:
                print(f"value[{v}]")
        else:
            print("<etc>")
            print(f"value[{px}]")
                
        

#%%
# [문제2] 함수 printlist()에서 전달 받은 인자에서 요소를 하나씩 출력하세요.
# 자료형에 맞게 하나씩 꺼내서 출력하세요.

printlist('리스트', [2,4,6,8,10])
printlist('튜플', (1,3,5,7,9))
printlist('셋', {10,20,30,40,50})
printlist('딕셔너리', {1:'하나',2:'둘',3:'Three'})

#%%
printlist("리스트, 튜플", [1,3,5,7],(2,4,6,8))
#%%
#def printlist(title, args):
#    print(f"arg({args})")
#    a = list(args)
#    for x in a
#       print(x)

#printlist('리스트', [2,4,6,8,10])


