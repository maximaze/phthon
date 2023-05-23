# packages : 디렉터리와 모듈로 구성
# 패스 : game.sound
# 모듈 : soundecho.py

# 최상위 폴더만 지정
# import folder
import game

# 풀패스를 지정해야 한다.
game.sound.soundecho.echo("안녕!")
