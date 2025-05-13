import random

# 60 ~ 240 사이의 랜덤한 분(minute) 값 생성
total_minute = random.randint(60, 240)
print(total_minute)

# 총 분을 시간과 분으로 나누기
hour = total_minute // 60    # 시간
minute = total_minute % 60   # 분

print(hour, minute)

# XXX분은 X시간 X분 입니다.
# print(total_minute + " minute is " + hour + "h " + minute + "min ")

# casting : 데이터 유형을 원하는 형태로 변경하고자 할 때 사용
# int(), float(), complex(), bool(), str()
print(int(4.92), int("43"))
print(float(4), float("43.43"))
print(str(4), str(45.22))
print(bool(1), bool("True"), bool(""))

# + 연산으로 문자열 연결 str로 자료형 변환
print(str(total_minute) + " minute is " + str(hour) + "h " + str(minute) + "min ")

# 문자열 연결 방식
txt = f"{total_minute} minute is {hour} h, min." #format string
print(txt)
