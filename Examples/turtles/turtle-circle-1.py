# 거북이 이동 예제
# 라이브러리 사용
import turtle   # 터틀 라이브러리
import math     # 수학함수 라이브러리

tp = turtle.Pen()

distance = 200
angle = 90

for n in range(4):
    tp.forward(distance)
    tp.right(angle)

tp.right(45)
# tp.goto(distance, -distance)
tp.goto(distance, distance * -1) 

tp.right(45 * 3)
tp.penup()
tp.forward(distance)
tp.right(45 * 3)
tp.pendown()
tp.goto(distance, 0)

# 사각형의 중앙에 원을 그려라
radius = distance // 2 # 정수나누기
tp.penup()
tp.goto(distance // 7 * 6, distance // 7 * 6 * -1) 
tp.pendown()
tp.circle(radius)


turtle.done()