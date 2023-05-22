# 예외처리
# try ~except

filename = "없는파일.txt"

try :
    file = open(filename, 'r') # 파일을 읽기용으로 오픈
except FileNotFoundError as e : # 모든 예외를 처리
    print(f"{filename} 파일이 없습니다.")
    print("예외발생:", e)
    
print("작업종료")





