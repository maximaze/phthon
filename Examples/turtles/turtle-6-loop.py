# 거북이 이동 예제
# 라이브러리 사용
import turtle


tp = turtle.Pen()

distance = 200
angle = 90

# 반복문을 사용해서 사각형 그리기
for n in range(4):
    tp.forward(distance)
    tp.left(angle)

turtle.done()