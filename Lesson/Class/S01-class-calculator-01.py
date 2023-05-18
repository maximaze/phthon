# 클래스(class)
# 청사진, 설계도
# 클래스에 의해서 생성된 객체는 서로 독립적이다.
# 클래스에 의해서 생성된 객체를 인스턴스라 한다.
#################################################
# self : 객체의 식별자, 생성자나 메소드 맨처음에 파라미터에 기술
# 속성 : 
#   - self.속성, 멤버변수, 없으면 새로 만듦, 있으면 사용
#   - 생성자가 아닌 메소드에서도 새로 만들 수 잇다.
# 생성자 : 객체가 생성될 때 호출 됨
# 소멸자 : 객체가 소멸될 때 호출 됨, 프로그램이 종료될 때

# 전자계산기 클래스 정의
class Calculator:
    def __init__(self): # 생성자
        print("생성자 호출")
        self.total = 0
        
    def __del__(self):  # 소멸자
        print("[소멸자] self({id(self)})")
        
    def add(self, num): # 메소드
        print("메소드 호출")
        self.total += num
        return self.total

# 객체 생성
calc = Calculator()

print(calc.add(10))
print(calc.add(20))
print(calc.add(30))


