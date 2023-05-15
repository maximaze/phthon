# 제어문(if)
# None은 참(True)이 아니다.
# None은 거짓(False)이 아니다.
# None은 아무것도 없다는 의미의 특별한 값.

thing = True
# thing = False

''' // is not False는 False가 아니다가 되기때문에 애초에 잘못된 조건이됨
if thing not is False:
    print('Thing is False')    
else:
    print('Thing is True')
'''
# not a is b // 그래서 사용하려면 이렇게 not과 is 사이에 넣어야함
if not thing is False:
    print('> Thing is True')    
else:
    print('> Thing is False')
