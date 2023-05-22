# 상속(inheritance)
"""
class 클래스이름(부모클래스):
    ...
"""
# 계산기 : 공통 클래스
# 중간중간에 들어가는 init는 제일 위에 존재하는 CalcProto에만 있어도 작동함
# 밑에는 상속된것들이니 없으면 기어올라와서 작동
# 근데 오류가 일어날 위험도가 있으니 추가하는걸 추천
class CalcProto():
    def __init__(self, initval):
        self.total = 0
        print("[CalcProto] __init__ : initval=", initval)
        
#%%
# 더하기 계산기
class CalcPlus(CalcProto):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
        print("[CalcPlus] __init__ : initval=", initval)
        
    def plus(self, num):
        self.total += num
        return self.total

#%%
# 빼기 계산기
class CalcMinus(CalcProto):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
        print("[CalcMinus] __init__ : initval=", initval)
        
    def minus(self, num):
        self.total -= num
        return self.total
    
#%%
# 다중상속 : 더하기, 빼기 기능을 가진 계산기
# 새로운 메서드 추가 : 곱하기, 나누기
class Calc(CalcPlus, CalcMinus):
    def __init__(self, initval):
        super().__init__(initval) # 부모의 생성자 호출
        print("[Calc] __init__ : initval=", initval)
        
    def multiple(self, num): # 곱하기
        self.total *= num
        return self.total
    
    def divide(self, num):   # 나누기
        self.total /= num
        return self.total

#%%
calc = Calc(10)
print("Calc()")
print('더하기(10):',calc.plus(10))
print('빼기(5):',calc.minus(5))
print('곱하기(3):',calc.multiple(3))
print('나누기(2):',calc.divide(2))

