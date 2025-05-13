# 파이썬에서 사용하는 기본 데이터 타입
a = "python"
print(a, type(a))

b = 123123123123
print(b, type(b))

c = 3.324
print(c, type(c))

d = 4j
print(d, type(d))

e = True  # 또는 False
print(e, type(e))

# 컬렉션 (데이터 집합체)
aa = [1, 2, 4, 5]
print(aa, type(aa))
print(aa[0])  # 접근 가능
aa[0] = "Apple"  # 변경 가능

# 튜플
bb = ("apple", "banana", "cherry")
print(bb, type(bb))
print(bb[0])  # 접근 가능
# bb[0] = "Apple" # 변경 불가능

# set
cc = {"apple", "banana", "cherry"}
print(cc, type(cc))
# print(cc[0])   # 접근 불가능

dd = {"name": "luffy", "age": 19}
print(dd["name"])