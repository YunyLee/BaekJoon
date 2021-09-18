# 백준 단계별 풀이 - 함수 - 4673 문제
# 생성자가 없는 셀프넘버를 출력하는 프로그램

natural_number = set(range(1,10001))
generated_number = set()

for i in natural_number:
    sum_number = 0
    for j in str(i):
        sum_number += int(j)
    generated_number.add(i+sum_number)

result = sorted(natural_number-generated_number)
for i in result:
    print(i)
