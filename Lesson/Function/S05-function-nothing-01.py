# 함수
# 아무 처리도 하지 않는 함수
# pass 키워드 사용
# 이유 : 아직 함수가 ㄹ처리해야 할 기능이 정의됮 않았지만
#        향후에 처리해야 할 필요가 있는 경우 사용하여
#        처리 로직에서 누락을 예방할 수 있다.
# 리턴값 : None
 
'''
자바 : 아무 처리도 하지 않는 함수
void nothing(){
    }
'''

# 정의
# 아무 동작도 하지 않고 건너 뜀
def nothing():
        pass

# 호출
print("nothing() 함수 호출")
result = nothing()

print("nothing() 함수 리턴값 : ", result)

