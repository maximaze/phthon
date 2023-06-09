# 인스턴스
# isinstance(객체, 자료형) -> True, False
# 

# type : 자료형을 알려 준다.
f = 0.1234
print('type:', type(f)) # float(실수형)

fs = str(type(f))
print('type:', fs)

# instance
print('instance:', isinstance(f, float))

ft = type(f) # float
print(isinstance(f, ft))
print(isinstance(f, type(f)))

print('instance:', isinstance(f, str))
