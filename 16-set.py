# set : 순서가 없고 중복 허용 안함

# 중복 허용 X
s1 = {1, 2, 4, 2}
print(len(s1), s1)

raw = [1, 4, 5, 1, 3, 1, 3, 4, 3, 5, 5]
s2 = set(raw)
print(s2)
print (99 in s2)

for v in s2 :
    print(v)

# 아이템 하나 추가
s2.add(6)
print(s2)

# 다른 컬렉션의 요소를 현재 set에 추가
s2.update(s1)
print(s2)

# 집합 개념 (합집합, 교집합, 차집합)
s3 = {1, 2, 6, 8, 9}
s4 = {1, 3, 6, 7}
s5 = s3.union(s4)

print(s3.union(s4)) # 합집합
print(s3 | s4)

print(s3.intersection(s4)) # 교집합
print(s3 & s4)

print(s3.difference(s4)) # 차집합
print(s3 - s4)

print(s3.symmetric_difference(s4))
print(s3 ^ s4)

arr = [1, 2, 3, 4, 5, 1, 3, 5]
v = list(set(arr))
print(v)
