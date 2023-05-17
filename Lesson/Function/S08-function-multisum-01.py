# 함수예제
# 가변 인자를 활용한 예제

# [문제] mulitsum() 함수를 완성하세요.
# choice : 
#   - 'add' : 더하기
#   - 'mul' : 곱하기

def multisum(choice, *args):
    if choice == 'add':
        print("<add>")
        for a in args[0:4]:
            result = 0
            for a in args:
                result += a
                print(f"a={a}, result={result}")
            return result
    elif choice == 'mul':
        print("<mul>")
        for a in args[0:4]:
            result = 1 
            for a in args:
                result *= a
                print(f"a={a}, result={result}")
            return result
    else:
        print("etc")

#%%
s1 = multisum('add', 1,2,3,4,5) # 모두 더하기
s2 = multisum('mul', 1,2,3,4,5) # 모두 곱하기

print('s1= ', s1)
print('s2= ', s2)

