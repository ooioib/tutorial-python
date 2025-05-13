# python의 함수 : 특정 역할을 수행하기 위한 코드 묶음
# 파이선에서 함수 만들기 : def 라는 키워드를 이용해서 function을 정의

# 함수 정의 : test 라는 이름의 함수 만들기
def test():
    print("test function called")  # 함수 호출 시 출력될 문장

# 함수 호출 : 위에서 만든 test 함수 실행
test()


# 매개변수에 기본값 지정 가능
# name 인자를 전달하지 않으면 기본값 "anonymous" 사용됨
def greet(name="anonymous"):
    print(f"Hello? {name}~")  # 인사 출력


greet("luffy")  # 인자를 전달해서 호출
greet()  # 인자를 생략해도 에러 없이 동작 (기본값이 있기 때문)


# 두 수를 더해서 결과를 리턴하는 함수
def add(n1, n2):
    return n1 + n2  # 덧셈 결과를 반환


# 함수 호출하고, 리턴값을 r에 저장
r = add(4, 5)

# 결과 출력
print(r)