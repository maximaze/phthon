# 거북이 이동 예제
# 라이브러리 사용
import turtle   # 터틀 라이브러리
import math     # 수학함수 라이브러리

tp = turtle.Pen()

start = 10  # 시작값
end = 100   # 종료값
step = 3    # 증가값

for x in range(start, end, step):   # 3부터 시작해서 99까지 3씩 증가
    tp.circle(x)
    tp.left(91)

turtle.done()