# 모듈 mod4 사용 예제

# import 모듈 as 별칭
import mod4 as mod

print('# 모듈 mod4 사용 예제')
print(f'add(10,20) -> {mod.add(10,20)}')
print(f'sub(10,100) -> {mod.sub(10,100)}')

# PI
print("PI : ", mod.PI)

# 반지름이 7인 원의 넓이는?
# case1 / 한줄로 처리도 가능
math = mod.Math()
cirarea = math.circlearea(7)
# cirarea = mod.Math().circlearea(7)
print("반지름이 7인 원의 넓이는?", cirarea)


# case2
class Math:
    def circlearea(self,r):
        return mod.PI * (r ** 2)
    
math = Math()
cirarea = math.circlearea(7)
print("반지름이 7인 원의 넓이는?", cirarea)






