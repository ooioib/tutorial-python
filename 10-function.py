# 매개변수를 넘길때, position 을 이용해서 넘길때, keyword를 이용해서 넘기는 방법도 있다.

# x, y 좌표를 받아서 어떤 사분면에 위치하는지 알려주는 함수
def guess_quadrant(x, y):
    if x > 0 and y > 0:
        return 1  # 1사분면
    elif x > 0 and y < 0:
        return 4  # 4사분면
    elif x < 0 and y > 0:
        return 2  # 2사분면
    elif x < 0 and y < 0:
        return 3  # 3사분면
    else:
        return 0  # x 또는 y가 0인 경우는 축 위이므로 0 리턴


# 함수 호출할 때 매개변수를 위치(position) 기준으로 전달
a = guess_quadrant(4, 2)

# 키워드(keyword) 방식으로 전달하면 매개변수 순서를 지키지 않아도 됨
b = guess_quadrant(x=-4, y=7)  # 매개변수 순서를 안지켜도 됨
c = guess_quadrant(y=10, x=1)

print(a, b, c)

# 위치 인자와 키워드 인자를 혼합해서 사용해도 됨
d = guess_quadrant(-3, y=4)
print(d)


# 특정 함수를 쓰다보면 매개변수가 꽤 많은 애들이 있는데,
# 그런 함수들은 매개변수 부분에 defaultValue들을 처리해두는 경우가 많아서
# 특정 인자만 전달하고자 할 때 보통 사용을 한다.

# 더치페이를 계산하는 함수
# price : 총 금액, already : 이미 낸 금액, person : 인원 수
# equal : True면 정확하게 나누고, False면 정수 나눗셈(몫만) 처리
def dutch_pay(price=0, already=0, person=0, equal=True):
    current = price - already  # 남은 금액 계산
    if equal:
        return current / person  # 정확하게 나누기
    else:
        return current // person  # 몫으로 나누기


# 모든 매개변수를 위치 방식으로 전달
r = dutch_pay(10000, 2000, 3, True)
print(r)

# 필요한 매개변수만 키워드 방식으로 전달 (기본값 활용)
r = dutch_pay(price=13000, person=3)  # dutch_pay(13000, person=3)
print(r)

# 일부만 기본값 사용 (equal은 기본값 True)
r = dutch_pay(13000, 0, 3)
print(r)


print(type(dutch_pay))

dp = dutch_pay  # 파이썬에서도 function 이 매개변수 전달되는 경우도 있음
print(dp(13000, person=2))