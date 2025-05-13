# python의 if statement

# input() 함수를 사용하면 입력을 받을 수 있고, 항상 문자열(str)로 반환됨
# 출력을 하면서 입력을 받을 수 있음
a = input("Your age?")
print(type(a))

# ===================================

fee = 1000

# 문자열로 받은 입력을 정수형(int)으로 변환 (형변환)
age = int(input("Your age?"))
print(type(a))

# 조건문: 나이가 20보다 크면 추가 요금 부과
if age > 20:
    fee += 500

print(f"your ticket price is {fee}")

# ===================================

fee = 1000
age = int(input("Your age?"))

if age > 20:
    print("20% additional charge occur")
    fee *= 1.2 # 요금의 1.2배 (20% 추가 요금)

print(f"your ticket price is {fee}")

# ===================================

fee = 1000
age = int(input("Your age?"))

if age > 20:
    print("20% additional charge occur")
    fee *= 1.2

elif age < 6:
    print("30 discounted")
    fee *= 0.7 # 요금의 70%

else:
    print("welcome")

print(f"your ticket price is {fee}")