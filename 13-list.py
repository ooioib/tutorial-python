my_list = ["luffy", "zoro", "nami", "sanji", "chopper", "franky"]
print(my_list)

# change
my_list[0]="Luffy"
print(my_list)

# 0~3
my_list[0:2] = ["Luffy", "Zoro"]
print(my_list)

# insert
my_list.insert(0, "Gurf")
print(my_list)

# remove
my_list.remove("sanji")
print(my_list)

my_list.pop(3) # index 생략시 맨 뒤 삭제
print(my_list)

del my_list[2]
print(my_list)

# clear
my_list.clear()
print(my_list)
