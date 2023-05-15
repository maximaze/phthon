# 딕셔너리 결합(update)
# 기존의 딕셔너리에 새로운 딕셔너리를 결합
# dict.update(newdict)

weeks = { 1:'월', 2:'화', 3:'수', 4:'목', 5:'금', 6:'토' }
sun = { 0:'일' }

print(weeks)

# 기존의 딕셔너리에 새로운 딕셔너리를 결합
# dict.update(newdict)
weeks.update(sun) # weeks + sun
print(weeks)

#
# TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
# weeks += sun


