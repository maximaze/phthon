# packages : 디렉터리와 모듈로 구성
# 패스 : game.sound
# 모듈 : soundecho.py

# 패키지에 있는 모든 모듈
# from package import *
from game.sound import *

# 패키지 이름 생략
# 모듈.함수()
soundecho.echo("안녕!")
