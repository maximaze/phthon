# 예외처리
# 제로(0)으로 나누기

x = 10
y = 0

try:
    # 블록 안에서 선언된 변수도 블록 밖에서 참조 가능(로컬변수가 아니다)
    z = 0
    # z가 선언되기 전에 오류 발생
    z = x / y
except ZeroDivisionError as e:
    print("예외발생 : ", e)
    print(f"x({x})의 값을 y({y})로 나누려고 했습니다.")
    

print(f"x={x}")
print(f"y={y}")
print(f"z={z}") # 블록안에서 선언 된 변수도 참조 가능







