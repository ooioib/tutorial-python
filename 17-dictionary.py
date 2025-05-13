# dictionary : 키(key)-값(value) 형태로 데이터를 저장하는 컬렉션

# car 딕셔너리 생성
car = {
    "brand" : "kia",
    "model" : "sorrento",
    "price" : 3500
}

# car의 타입 출력
print(type(car))

# movie 딕셔너리 생성
movie = dict(title = "Mine-craft", realease = 2025)
print(type(movie))

# car와 movie 전체 내용 출력
print(car, movie)

# 딕셔너리 안에 있는 항목 개수 출력
print(len(car), len(movie))

# kia 값이 있는지 확인 => False
print("kia" in car)

# brand 키가 있는지 확인 => True
print("brand" in car)

# brand 키에 해당하는 값 출력 => 'kia'
print(car["brand"])

# 딕셔너리를 반복문으로 순회하면서 키와 값을 출력
for x in car:
    print(x, car[x])

# 값들만 따로 가져오기
print(car.values())
for v in car.values():
    print(v)

# 키-값 쌍을 튜플 형태로 가져오기
print(car.items())

# key, value 쌍으로 반복문 돌리기
for key, values in car.items():
    print(key, values)

# 키가 brand인 항목 삭제
del car["brand"]
print(car)

# 키 목록 가져오기
print(car.keys())

# price 값 변경
car["price"] = 4000
print(car)

# 딕셔너리에 새 키-값 쌍 추가
car["rating" ] = 9.2
print(car)

# 여러 개의 항목을 한 번에 추가하거나 수정
car.update({"rating" : 9.1, "promotion" : True})
print(car)