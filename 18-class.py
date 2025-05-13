# Circle 클래스 정의
class Circle:
    # 생성자 함수 : 객체가 생성될 때 자동으로 실행됨
    def __init__(self, radius=1):
        self.radius = radius  # 객체에 반지름 값을 저장

    # 객체를 출력했을 때 보여질 문자열 설정
    def __str__(self):
        return f"radius = {self.radius}"

    # 원의 둘레 계산
    def perimeter(self):
        return self.radius * 2 * 3.14  # 2 * π * r

# 반지름이 9인 Circle 객체 생성
c1 = Circle(9)
print(c1.radius)

# c1의 둘레 출력
print(c1.perimeter())   # 2 * 3.14 * 9 = 56.52
print(c1)

c1.radius = 10
c1.corn = True
