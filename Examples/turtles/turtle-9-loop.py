# 거북이 이동 예제
# 라이브러리 사용
import turtle


tp = turtle.Pen()

# 리스트(list): 데이터 목록
# 대괄호([])로 데이터를 감쌈
# colors = ['red', 'yellow', 'blue', 'green'] # 4개 목록값을 가지고 있음
colors = ['red', 'black', 'blue', 'green'] # 4개 목록값을 가지고 있음
# print(colors[0])    # 리스트의 첫번째 요소를 참조
# print(colors[1])
# print(colors[2])
# print(colors[3])

# colors 목록에서 요소를 하나씩 꺼내서 color변수 넣어준다.
# 목록에 들어있는 요소의 갯수만큼 반복(4번 반복)
for color in colors:    
    print(color)

# 다중라인 주석:
# 시작(""")은 쌍따옴표를 첫 컬럼을 시작하고 종료
distance = 100
angle = 95

for n in range(distance):   # n값은 0부터 99까지 증가
    tp.pencolor(colors[n % 4])  #  나머지연산으로 0~3까지 반복
    tp.forward(n)
    tp.left(angle)

turtle.done()
# 다중라인 주석 종료(""")