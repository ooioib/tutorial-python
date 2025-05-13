import random

my_list = ["luffy", "zoro", "nami", "sanji", "chopper", "franky"]
print(my_list)

# loop
for x in my_list:
    print(x)

print(len(my_list))

for i in range(len(my_list)):
    print(i, my_list[i])

# ============================================

my_number = [145, 4, 2, 5, 14, 5, 58, 1, 5]

# 짝수 값만 가진 배열 만들기 (filter)
even_number = []
for num in my_number:
    if num % 2 == 0:
        even_number.append(num)
print(even_number)

# 현재 기본 값을 2배한 배열 만들기 (map)
double_number = []
for num in my_number:
    double_number.append(num * 2)
print(double_number)

# 기존 배열을 토대로 이전 작업들을 간단하게 할 수 있는 문법
copy_number = [num for num in my_number]
print(copy_number)

copy_number_2 = [print(num) for num in my_number]
print(copy_number_2) # None == Null


double_number_2 = [num * 2 for num in my_number]
print(double_number == double_number_2)

even_number_2 = [num for num in my_number if num % 2 == 0]
print(even_number == even_number_2)

arr = [random.randint(10, 100) for num in range(1, 11)]
print(arr)

def test():
    print("test")

r = test()
print(r)