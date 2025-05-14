# 사람들의 이름과 나이를 담은 리스트 (각 요소는 딕셔너리 형태)
data = [
    {"name": "윤형호", "age": 19},
    {"name": "김병재", "age": 29},
    {"name": "문진수", "age": 27}
]

# age 값을 추출해 반환
def convert_to_age(item):
    return item["age"]

# data 리스트의 첫 번째 요소의 나이를 출력
print(convert_to_age(data[0]))

# 나이를 기준으로 오름차순 정렬
data.sort(key=lambda item: item["age"])

print(data)
