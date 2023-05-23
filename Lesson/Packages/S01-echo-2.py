# packages : 디렉터리와 모듈로 구성
# 패스 : game.sound
# 모듈 : soundecho.py

# from packages import module
from game.sound import soundecho

# 패키지 이름 생략
# 모듈.함수()
soundecho.echo("안녕!")
