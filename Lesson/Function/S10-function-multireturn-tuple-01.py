# 함수 예제
# 리턴: 다중 리턴, 튜플형으로 리턴

# n까지의 총합과 평균
def multireturn_tuple(n):
    result = [] # 리스트
    total = 0
    
    for x in range(n+1):
        total += x
    
    avg = total / n
    result.append(avg)
    result.append(total)
    return tuple(result)

#%%

result = multireturn_tuple(10)
print("result = ", result, type(result))
print("총합 = ", result[0])
print("평균 = ", result[1])

tot, avg = result
print("Unpacking result")
print("총합 = ", tot)
print("평균 = ", avg)