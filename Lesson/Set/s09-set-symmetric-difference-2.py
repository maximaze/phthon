# 대칭 차집합 : 한 쪽에는 있지만 양쪽 모두에 있지 않는 멤버
# set.symmertic_difference

a = { '서울', '대전', '대구', '부산'}
b = { '서울', '대전', '대구', '부산', '전주', '목포'}
c = { '서울', '대전', '대구', '부산', '제주'}

sd2 = b.symmetric_difference(c)
print(sd2)
print(c - b)
print(b - c)
sd3 = (c - b) | (b - c)
print(sd3)