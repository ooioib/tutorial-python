# for문 : 다른 언어의 일반 for문보다 for-each 스타일
# 리스트나 문자열 등 순회 가능한 데이터에서 요소 하나씩 꺼내서 반복

names = ["luffy", "zoro", "sanji", "nami", "usop"]
for n in names:  # 리스트의 각 요소를 하나씩 꺼내서 n에 담음
    print(n)
    if n == "sanji":  # 조건이 맞으면 반복 중단
        break

print("---------------------------------------")

# 문자열도 반복 가능 (문자열은 문자들의 리스트처럼 동작)
txt = "programming"
for x in txt:  # 문자 하나씩 꺼내서 x에 담음
    print(x)

# 일반적인 숫자 반복을 하고 싶을 때는 range() 함수 사용
# range(5)는 0부터 4까지 숫자 생성
print(range(5))  # 출력: range(0, 5), 실제 출력은 리스트처럼 보이지 않음
print(type(range(4)) )  # range 객체의 타입 확인

# range(start, end, step) 형식
# 3부터 시작해서 10보다 작을 때까지, 2씩 증가하면서 반복
for x in range(3, 10, 2):
    print(x)

# 반복 횟수만 중요하고 값은 필요 없을 때는 언더바(_) 사용
for _ in range(5):
    print("python")
