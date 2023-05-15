# 부분집합
# set.issubset(set)
# a.issubset(b) : a는 b의 부분집합인가?

a = { '서울', '대전', '대구', '부산'}
b = { '서울', '대전', '대구', '부산', '전주', '목포'}
c = { '서울', '대전', '대구', '부산', '제주'}

# a는 b의 부분집합인가?
# a는 b에 모두 포함되므로 True
s1 = a.issubset(b)
print(s1)

# c는 b의 부분집합인가?
# '제주'가 b에 없기 때문에 False
s2 = c.issubset(b)
print(s2)