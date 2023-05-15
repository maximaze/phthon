# 대칭 차집합 : 한 쪽에는 있지만 양쪽 모두에 있지 않는 멤버
# set.symmertic_difference

b = { '서울', '대전', '대구', '부산', '전주', '목포'}
c = { '서울', '대전', '대구', '부산', '제주'}

sd2 = b.symmetric_difference(c)
print('결과1:', sd2)

print('단계1', c - b)
print('단계2:', b - c)

sd3 = (c - b) | (b - c)
print('결과2:', sd3)

sd4 = b ^ c
print('결과3:', sd4)