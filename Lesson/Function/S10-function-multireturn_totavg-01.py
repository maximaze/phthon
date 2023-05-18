# 함수 예제
# 가변 인자를 활용한 예제
# 리턴: 다중 리턴, 튜플형으로 리턴

# 가변인자의 총합과 평균
def multireturn_totavg(*args):
    total = 0
    
    for x in args:
        total += x
    return total, total / len(args)
#%%

# unpacking <- tuple
tot, avg = multireturn_totavg(1,2,3,4,5)    # 평균
print("# unpacking <- tuple")
print('총합=', tot)
print('평균=', avg)

#%%

# tuple
result = multireturn_totavg(1,2,3,4,5)

tot,avg = result

print(f"# result : {result}, {type(result)}")
print('총합=',tot)
print('평균=',avg)

#%%

result = multireturn_totavg(1,2,3,4,5)
print(f"# {type(result)} 인덱스로 접근")
print('총합=',result[0])
print('평균=',result[1])
