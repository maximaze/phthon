# 예외처리
# 제로(0)으로 나누기 : ZeroDivisionError
# 선언되지 안은 변수에대한 예외처리 : NameError

x = 10
y = 0

try:
    z = x / y
except ZeroDivisionError as e:
    print("예외발생 : ", e)
    print(f"x({x})의 값을 y({y})로 나누려고 했습니다.")
    

print(f"x={x}")
print(f"y={y}")

# 선언되지 않은 변수에 대한 예외처리
try:
    print(f"z={z}")
except NameError as e:
    print("예외발생 : 변수(z)가 선언되어 있지 않습니다.")
    print(e)







