# 대칭 차집합 : 한 쪽에는 있지만 양쪽 모두에 있지 않는 멤버
# sd = set(a).symmertic_difference(b)
# sd = a ^ b

a = { '서울', '대전', '대구', '부산'}
b = { '서울', '대전', '대구', '부산', '전주', '목포'}
c = { '서울', '대전', '대구', '부산', '제주'}

sd1 = a.symmetric_difference(b)
print(sd1)
print(b - a)
print(a - b)

# 차집합, 합집합을 결합해서 대칭 차집합을 구함
sd2 = (b - a) | (a - b)
print(sd2)

