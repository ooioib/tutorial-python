# comparison operator 비교 연산
# ==, !=, >, <, >=, <=
print(4 == 4)
print('Apple' == 'Apple')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

# logical operator(논리연산)
# end(&&), or(||), not(!)
x, Y = 14, 19
result = (x > 0 and x < 0)
print(result)
print(not result)
print(x >= 0 and x <= 20)
print(0 <= x <= 20)

# membership operatort
# in : 포함 되었다면 true
# not in : 포함 되어있지 않다면 True
print()
print('java' in 'javascript')
print(1 in [11, 2, 3, 4, 5, 1])

# identity operator : 객체 동등성 체크
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True
print(a is b)  # False
print(a is c)  # True

# 3항 연산 ? :
num = 4
r = "even" if num % 2 == 0 else "odd"
print(r)  # even


