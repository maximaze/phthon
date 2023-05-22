# 예외처리
# try ~ except ~ else ~ finally
# finally : 예외에 관계없이 항상 수행된다.
# 예외가 발생하여 예외처리릏 ㅏㄴ 후 수행
# else :  예외가 발생되지 않으면 처리되는 블록, finally 구문보다 앞에 기술해야 한다.(옵션)
# finnaly는 마무리 작업을 해야 할 것이 잇으면 사용 할 수 있다.(옵션)

lst=[1,2,3,4,3]
print(lst)

try : 
    for x in lst:
        y = x / lst[x]
        print(f"x({x}) / {lst[x]} -> {y}")
except (ZeroDivisionError,IndexError) as e:
    print("[예외발생]",e)
else:
    print("[else] 예외가 발생되지 않고 정상적으로 치러 했습니다.")
finally:
    print("[finally] 처리 종료")
    
print("[작업종료]")