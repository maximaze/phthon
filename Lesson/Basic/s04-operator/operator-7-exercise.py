# [문제3]
# 한 달 급여가 400만원이다.
# 분기별로 보너스가 월 급여의 30%가 지급된다.
# 세금은 월 수령액의 3%이다.
# 보너스에 대한 세금은 없다.
# 월 세후 수령액은 얼마인가?
# 연 수령액(세후 총 수령액)은 얼마인가?
# 총 세금은 얼마인가?

# 한달 급여
a = 4000000
print('한달 급여=',a)

# 분기별 보너스
b = 4000000*0.3
print('분기별 보너스=',b)

# 세금
c = a*0.03
print('세금 =',c)

# 월 세후 수령액
d = a-c
print('월 세후 수령액=',d)

# 연 수령액
e = (12*d)+(4*b)
print('연 수령액=',e)

# 총 세금
f = c*12
print('총 세금=',f)

print('---------------------------------')
# 한 달 급여
salary = 4000000
print("급여: ", salary)

# 분기별 보너스
bonus = salary * 0.3
print("분기별 보너스: ", bonus)

# 세금
tax = salary * 0.03
print("세금: ", tax)

# 월 수령액
month_salary = salary - tax
print('월수령액', month_salary)

# 총 연봉
total = salary * 12
total += bonus * 4
print("총연봉: ", total)

# 연 수령액
year_salary = month_salary * 12
year_salary += bonus * 4
print("연수령액: ", year_salary)

