# 딕셔너리

# 기본형
poetry = {
    "title": "진달래",
    "author": "김소월",
    "content": "나 보기가 역겨워 가실 때에는 ..."
}

print(poetry)

# 키를 통해 값을 바꿈
poetry['title'] = '진달래 꽃'

# 키를 통해서 값을 꺼냄
print(poetry['title'])
print(poetry['author'])
print(poetry['content'])
