# 문자열(String)
# 변수 이름과 구별되며 리터럴(literal)
# 문자열은 데이터로서 문자들의 집합
# 큰 따옴표(")로 감싸서 문자열이라는 것을 알린다.
# 작은 따옴표(')로 감싸서 문자열이라는 것을 알린다.

# 빈 문자열 생성
hello = ""
world = ''

# 포멧의 맨 앞에 f를 지정하지 않으면
# format이 적용되지 않고 문자열 그대로 출력된다.
print('hello=[{hello}]') # hello=[{hello}]

print(f'hello=[{hello}]')
print(f'world=[{world}]')

