back = int(input("백엔드 구현 능력(1 ~ 100) "))
front = int(input("프론트엔드 구현 능력(1 ~ 100) "))
data = int(input("데이터 분석 능력 (1~100) "))

# 세 항목 모두 40 미만
if back < 40 and front < 40 and data < 40:
    print("기초부터 다시 시작하세요")

else:
    if back >= front and back >= data:
        print("백엔드 개발자로 성장가능!")
        if front >= 70:
            print("풀스택 개발자로도 충분한 역량 보유!")

    elif front >= back and front >= data:
        print("프론트엔드 개발자로 성장가능!")

    else:
        print("데이터 분석 개발자로 성장가능!")


# match statement는 switch - case랑 비슷한 구문