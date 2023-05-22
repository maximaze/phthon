# 예외처리
# 파일이 없는 경우

filename = "없는파일.txt"

file = open(filename, 'r') # 파일을 읽기용으로 오픈
if file == None: # 리턴값으로 잡을 수 없다.
    print(f"{filename} 파일이 없습니다.")
    
# FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'

print("작업종료")





