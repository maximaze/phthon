# 상속(inheritance)
"""
class 클래스이름(부모클래스):
    ...
"""

# 더하기 계산기
class CalcPlus():
    def __init__(self):
        self.total = 0
    
    def plus(self, num):
        self.total += num
        return self.total

#%%
# 빼기 계산기
class CalcMinus():
    def __init__(self):
        self.total = 0
        
    def minus(self, num):
        self.total -= num
        return self.total
    
#%%
# 다중상속 : 더하기, 빼기 기능을 가진 계산기
# // 자바에는 없는 개념
class Calc(CalcPlus, CalcMinus):
    pass

#%%
# 더하기 객체
plus = CalcPlus()
print('더하기:',plus.plus(10))
print('더하기:',plus.plus(20))

# AttributeError: 'CalcPlus' object has no attribute 'minus'
# 부모한테서 자식이 가져올수는 있어도 자식한테 부모가 가져올순 없으니
# print('더하기:',plus.minus(5))

#%%
# 빼기 객체
minus = CalcMinus()
print('빼기:',minus.minus(10))
print('빼기:',minus.minus(5))

# 동일한 부모가 되어서 상속이 안되어 사용이 불가
# print('빼기:',minus.plus(10))

#%%
calc = Calc()
print("Calc()")
print('더하기:',calc.plus(10))
print('빼기:',calc.minus(5))

