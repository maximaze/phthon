# 함수
# 가변인자 : 함수의 전달되는 파라미터가 0개 이상으로 여러개가 전달
# 함수인자 앞에 아스터리스크(*)를 넣음
# 가변인자형 : 튜플(Tuple)로 전달

# 가변인자로 전달 된 모든 값을 더하는 함수
def sum(*args):
    print(f"function -> sum({args}), type({type(args)}), len({len(args)})")
    result = 0
    for a in args:
        result += a
        print(f"a={a}, result={result}")
    return result

#%%
# 함수호출 : 인자의 갯수를 다양하게 전달
print(sum())            # 인자를 전달하지 않음(없음)
print(sum(10))          # 인자를 1개 전달
print(sum(1,3,5,7,9))   # 인자를 5개 전달




