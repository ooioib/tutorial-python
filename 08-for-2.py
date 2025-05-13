# for - else : for-else의 else는 정상 종료시에만 작동

# for문 반복: 0부터 9까지 숫자 생성
for n in range(10):
    if n == 3:  # n이 3이면 반복 중단
        break
    print(n)

# else는 반복이 끝까지 잘 돌아갔을 때만 실행됨
# 위에서는 break 때문에 실행 안 됨
else:  # break가 없었을 경우에만 실행
    print("finish")
