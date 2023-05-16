# 거북이 이동 예제
# 라이브러리 사용
import turtle


tp = turtle.Pen()

distance = 100
angle = 95

for n in range(distance):   # n값은 0부터 99까지 증가
    tp.forward(n)
    tp.left(angle)

turtle.done()