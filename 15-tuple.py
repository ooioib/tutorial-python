# tuple : 순서가 있지만 값을 바꿀 수 없는 자료형 (읽기 전용 배열 느낌)
# 값을 수정할 수 없는 고정된 데이터 묶음

t1 = ("fire", "water", "earth", "wind", "Fire")
print(t1)
print(t1[0])           # 첫 번째 요소 출력 ("fire")
# t1[0] = "Fire"       # 이렇게 값을 바꾸는 건 불가능 (오류 발생)
print(len(t1))         # 튜플의 길이 출력 (요소 개수)

# 튜플 요소 하나씩 출력
for v in t1:
    print(v)

t2 = ("light", "dark")
t3 = t1 + t2            # 튜플끼리 더하면 이어붙이기 가능
print(t3)

# 특정 값이 튜플에 있는지 확인
print("fire" in t2)