import sys
sys.stdin = open('input_8393.txt', 'r')

# 백준 단계별 풀이 - for문 - 8393 문제
# 1부터 N까지의 합을 구하는 문제

N = int(input())
n_sum = 0

for i in range(1,N+1):
    n_sum += i
print(n_sum)