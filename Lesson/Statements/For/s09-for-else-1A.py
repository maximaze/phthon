# 반복문(for)
# for ... else
# for문에서 break를 발견하지 못하면 else 실행

scores = [0,100,99,80,-10,99,110]
tot = 0
success = False

# for문에서 break를 발견하지 못하면 else 실행
for score in scores:
    if score < 0 or score > 100:
        break # 비정상처리
    tot += score
    print(score)
else: # 정상처리
    success = True

if success:
    print('데이터를 정상적으로 처리했습니다.')
else:
    print('데이터를 정상적으로 처리하지 못했습니다.')

print('점수의 합:', tot)
print('작업완료')