import sys
sys.stdin = open('input_11720.txt', 'r')

# 백준 - 단계별로 풀어보기 - 문자열 - 11720번 문제
# 숫자를 모두 합해서 출력하기

N = int(input())
N_LIST = input()

n_sum = 0
for i in N_LIST:
    n_sum += int(i)

print(n_sum)

# print(sum(map(int,input()))) 이렇게 한줄로 간단히 구현 가능