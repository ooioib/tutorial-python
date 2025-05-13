# string : 문자열, 홀따옴표, 쌍따옴표로 묶어서 표기
a = "python"
b = 'python'

# 문자열 길이는 len이라는 built-int function을 이용
print(len(a))
arr = [1, 12, 44, 43, 32, 65, 234, 245, 635, 3456, 7454]
print(len(arr))  # len 함수는 나중에 컬렉션 유형에도 사용 가능

# 내부적으로는 문자들의 집합 형태로 관리되는 list 구조이기 때문에 slicing
x = a[2:5]  # 인덱스 2부터 4까지 추출
print(x)
print(arr[1:4]) # 인덱스 1부터 3까지 출력
print(a[:4], a[2:]) # 처음부터 3까지, 2부터 끝까지

# string concat
print("Hello, " + "Python")
a += "! Nice to meet you"
print(a)

# 일반 프로그래밍 언어와 비슷하게 string 가지고 했던 작업들 다 메소드로 존재함
# string modify method
a = "Hello, Python"
print(a.upper())  # 대문자로 변환
print(a.lower())  # 소문자로 변환
print(a.replace("Python", "Java"))  # 특정 문자열 대체
print(a.split(", "), type(a.split(","))) # 문자열 분리(split), 구분자 기준으로 나눠서 리스트로 반환
