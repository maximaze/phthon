# 함수 : 람다식

#%%
# 콜백 함수
# words : 처리해야 할 데이터
# func  : 처리할 로직
def soundwonder(words, callback):
    for word in words:
        print(callback(word)) # 콜백함수 실행

words = ['hi', 'good', 'oh', 'nice']
    
#%%
# 일반 함수

# 첫문자를 대문자로 바꾸고 문자열의 끝에 감탄사(!)를 붙여서 출력
def wonder(word):
    return word.capitalize() + '!'

print("#일반함수")
soundwonder(words, wonder)


#%%
# 람다식 : 콜백함수로 익명함수로 전달
print("#람다함수")
soundwonder(words, lambda word : word.capitalize() + "!!!")
    
    