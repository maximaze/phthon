# 예외처리
# 예외 객체 만들기
# Exception : 예외처리 기반 클래스
# Exception을 상속하여 사용자 예외 클래스를 정의 할 수 있다.

# 사용자 정의 예외 클래스
class BirdException(Exception):
    pass

# 함수 : 파라미터의 전달된 값이 'dead'이면 예외발생
def HiBird(hi):
    if hi == 'dead':
        raise BirdException("버드가 죽었습니다.")
    print("OK!", hi)

# 예외처리    
try:
    HiBird('안녕!!!') # 정상
    HiBird('dead')    # 예외발생
except BirdException as e:
    print("[BirdException]", e)

