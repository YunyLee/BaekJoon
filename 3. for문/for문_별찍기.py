import sys
sys.stdin = open('input_2438.txt', 'r')

# 백준 단계별 풀이 - for문 - 2438 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())
star = '*'

for i in range(1, N+1):
    print(i * star)