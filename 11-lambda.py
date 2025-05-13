# lambda function : 간단한 기능을 구현하고자 할 때 사용할 수 있는 함수
# 람다로 만드는 function은 작업문을 하나만 가질 수 있다.
# def ____ (a) :
# return a**a


my_pow = lambda a: a ** 2
r = my_pow(3)
print(r)

my_add = lambda a, b: a + b
print(my_add(3, 4))


# ===================================

# 매개변수로 함수를 넘겨야 할 때가 있는데, 이 때 유용하게 사용 가능
def my_multi(a, b):
    return a * b


# 기본적으로 List의 sort는 오름차 정렬이나, function을 넘기면 절대값으로 정렬이 됨
my_multi2 = lambda a, b: a * b
data = [1, -3, 4, 55, -2, 1, 4]
data.sort(key=lambda v: v if v > 0 else -v)
print(data)

data = [1, -3, 4, 55, -2, 1, 4]


def custom_sort(v):
    if v > 0:
        return v
    else:
        return -v


# ===================================

data.sort(key=lambda v: v if v > 0 else -v)
print(data)

skills = ["python", "java", "javascript", "sql"]
skills.sort()
print(skills)

# 문자열 길이에 따라 sort 되게
skills = ["python", "java", "javascript", "sql"]
def custom(s):
    return len(s)
skills.sort(key=lambda s: len(s))
print(skills)
skills.sort(key=lambda s: len(s), reverse=True) # 역정렬 (기본값 False)
print(skills)