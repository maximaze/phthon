# 상속(inheritance)
"""
class 클래스이름(부모클래스):
    ...
"""
# 계산기 : 공통 클래스
class CalcProto():
    def __init__(self, initval):
        self.total = 0
        
#%%
# 더하기 계산기
class CalcPlus(CalcProto):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
    
    def plus(self, num):
        self.total += num
        return self.total

#%%
# 빼기 계산기
class CalcMinus(CalcProto):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
        
    def minus(self, num):
        self.total -= num
        return self.total
    
#%%
# 다중상속 : 더하기, 빼기 기능을 가진 계산기
# // 자바에는 없는 개념
class Calc(CalcPlus, CalcMinus):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
        
    def multiple(self, num): # 곱하기
        self.total *= num
        return self.total
    
    def divide(self, num):  # 나누기
        self.total /= num
        return self.total

#%%
calc = Calc()
print("Calc()")
print('더하기(10):',calc.plus(10))
print('빼기(5):',calc.minus(5))
print('곱하기(3):',calc.multiple(3))
print('나누기(2):',calc.divide(2))

