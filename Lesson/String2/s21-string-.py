# 문자열정리
# 문자열.center(길이)
# 문자열.ljust(길이)
# 문자열.rjust(길이)

# 한글은 한 문자로 취급되지만 간격을 2문자로 차지
text = "안녕"
print(f"123456789123567890")
print(f"[{text.center(10)}]") # 가운데정렬
print(f"[{text.ljust(10)}]") # 왼쪽정렬
print(f"[{text.rjust(10)}]") # 오른쪽정렬

text="Hello"
print(f"1234567891234567890")
print(f"[{text.center(10)}]") # 가운데정렬
print(f"[{text.ljust(10)}]") # 왼쪽정렬
print(f"[{text.rjust(10)}]") # 오른쪽정렬

textcenter = text.center(10)
print(f"textlen=({textcenter}), len={len(textcenter)}")
print(f"[{textcenter}.strip()] -> ({textcenter.strip()})")








