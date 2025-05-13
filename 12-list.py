# list : 타 언어의 배열같은 느낌의 컬렉션 (파이썬에서는 list외에 tuple, set, dictionary 도 있음)

# 직접 선언
my_list = ["luffy", "zoro", "nami", "sanji", "chopper", "franky"]
print(len(my_list))

my_list2 = list(["luffy", "zoro", "nami", "sanji", "chopper", "franky"])
print(my_list2)

my_list3 = []
my_list4 = list()
print(my_list3, my_list4)

my_list5 = list({"fire", "water", "earth"})
print(my_list5)

# access items
print(my_list[0])
print(my_list[-3])  # negative indexing (음수가 나오면 뒤에서 부터 위치)

# slicing
print(my_list[2:])
print(my_list[:5])
print(my_list[3:5])
print(my_list[-5:-3])
print(my_list[:])  # 전부 출력

# present check
print("ace" in my_list)  # True or False

# add item
my_list.append("robin")
print(my_list)

# 이중 배열로 들어감
my_list.append(my_list5)
print(my_list)

# 요소 추가
my_list.extend(my_list5)
print(my_list)

# extend는 +=로도 가능
my_list += my_list5
print(my_list)
