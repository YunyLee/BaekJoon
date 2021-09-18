import sys
sys.stdin = open('input_1157.txt', 'r')

# 백준 - 단계별로 풀어보기 - 문자열 - 1157번 문제
# 가장 많이 사용된 알파벳을 대문자로 출력하기(여러개면 ? 출력)

WORD = input().upper() #모두 대문자로 변환
exist_dict=dict()

for i in WORD:
    if i not in exist_dict:
        exist_dict[i] = 1
    else:
        exist_dict[i] += 1

max_cnt = 0
max_key = ''

for key, value in exist_dict.items():
    if max(exist_dict.values()) == value:
        max_cnt +=1
        max_key = key
if max_cnt >= 2:
    print('?')
else:
    print(max_key)