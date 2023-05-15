# 딕셔너리 함수
# 딕셔너리의 키 목록 : dict.keys()
#   -> class dict_keys
#-----------------------------------------------------
# return = dict.get(key)
#   - key가 없으면 None 리턴 
#   - None : 존자하지 않음을 의미하는 키워드
#-----------------------------------------------------
# return = dict.get(key, default)
#   - key가 없으면 default에 지정된 값이 리턴 

cust = {
    'name': '김수리',
    'tel' : '010-1234-5678'
}

print(cust)

# 딕셔너리의 키 목록
ck = cust.keys()
print(ck)


# 존재하지 않는 키로 검색을 하면 오류: 멈춤
# KeyError: 'addr'
# print('주소', ':', cust['addr']) 

# 존재하지 않는 키로 검색을 하면 결과가 None
# 프로그램이 종료되지 않는다.
# None : 값이 없음, 비어 있음
print('주소', ':', cust.get('addr')) # None

print('주소가 없는가? ', cust.get('addr') == None) # True


# 키가 존재하지 않으면 디폴트로 지정된 값을 리턴
defaddr = '주소가 없습니다.'
print('주소 :', cust.get('addr', defaddr)) 
print('주소 :', cust.get('addr', '주소가 없습니다.'))

# 
addr = cust.get('addr')
if addr == None:
    print('주소가 없습니다. 주소를 입력하세요')