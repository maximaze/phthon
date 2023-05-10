# 16진수(hexa-decimal)
# 0x or 0X : 0xff, 0XFF
# 
# 비트(bit) : 0, 1
# 니블(nibble) : 4비트
# 바이트(byte) : 8비트
# 10진수 : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 16진수 : 1 2 3 4 5 6 7 8 9  a  b  c  d  e  f 
# 16진수 : 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F 

# 1바이트로 최대 표현할 수 있는 값
# 16진수 : 4개의 비트가 한 단위로 구성
#  2진수: 1111 1111
# 16진수: 0xff 0XFF 0xFF
# 10진수: 255

# 2바이트
#  2진수: 1111 1111 1111 1111
# 16진수: 0xffff
# 10진수 : 65535
#  8진수 : 0o177777

d = 255
h = 0xff
H = 0XFF
hh = 0xFF
h2 = 0Xff

print('d=',d)
print('h=',h)
print('H=',H)
print('hh=',hh)
print('h2=',h2)