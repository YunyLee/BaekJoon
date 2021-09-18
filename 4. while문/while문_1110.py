
# 백준 단계별 풀이 - while문 - 1110문제
# 원래 수로 돌아올 때까지 연산을 반복하는 문제

N = int(input())
num = N # 가장 중요한 포인트 여기서 다른곳에 N값을 넣어주는 것!!
cnt = 0

while True:
    a = num//10
    b = num%10
    c = a + b
    num = (b*10) + (c%10)

    cnt += 1
    if num == N:
        break
    else:
        continue
print(cnt)
