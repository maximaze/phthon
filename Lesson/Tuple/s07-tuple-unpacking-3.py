# 튜플 언패킹(Unpacking)
# 튜플의 갯수와 변수의 갯수가 같아야 한다.

jobs = '요리사', '교사', '사무원'
print(type(jobs), jobs)

# 튜플의 갯수와 변수의 갯수가 같지 않으면 오류
# ValueError: too many values to unpack
#chef, teacher = jobs

# 생략 : underscore(_)
# unpacking 갯수를 맞춤
print("#3번째 생략")
chef, teacher, _ = jobs
print(chef)
print(teacher)
# print(officer)

print("#2번째 생략")
chef, _, officer = jobs
print(chef)
# print(teacher)
print(officer)

print("#전체 생략")
_, _, _ = jobs

# ValueError: not enough values to unpack (expected 4, got 3)
# job1, job2, job3, job4 = jobs
