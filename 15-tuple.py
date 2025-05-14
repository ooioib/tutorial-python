# tuple : 순서가 있지만 값을 바꿀 수 없는 자료형 (읽기 전용 배열처럼 사용)
# 값을 수정할 수 없는 고정된 데이터 묶음

t1 = ("fire", "water", "earth", "wind", "Fire")  # 문자열 요소를 가진 튜플 생성
print(t1)  # 전체 튜플 출력
print(t1[0])  # 첫 번째 요소 출력 ("fire")

# 튜플은 값을 바꿀 수 없음 => 아래 코드는 오류 발생
# t1[0] = "Fire"

print(len(t1))  # 튜플의 길이 출력 (요소 개수)

# 튜플의 각 요소를 하나씩 출력
for v in t1:
    print(v)

# 또 다른 튜플 생성
t2 = ("light", "dark")

# 튜플끼리 더하면 연결되어 하나의 새로운 튜플 생성됨
t3 = t1 + t2
print(t3)

# 특정 값이 튜플에 포함되어 있는지 확인 (결과는 True 또는 False)
print("fire" in t2)  # "fire"는 t2에 없으므로 False 출력

# 튜플은 괄호 없이도 만들 수 있음 (자동으로 튜플로 인식됨)
pos = 1, 4
print(type(pos))  # <class 'tuple'> 출력됨

# 두 수를 나눈 몫과 나머지를 튜플로 반환하는 함수 정의
def divide(a, b):
    return a // b, a % b  # 몫과 나머지를 튜플로 묶어서 반환

# 함수 실행 결과를 하나의 변수로 받을 수도 있고
r = divide(54, 32)
print(r)  # (1, 22) 출력됨

# 두 개의 변수로 나눠서 받을 수도 있음 (튜플 언패킹)
a, b = divide(10, 3)
print(f"a={a}, b={b}")  # a=3, b=1 출력됨
