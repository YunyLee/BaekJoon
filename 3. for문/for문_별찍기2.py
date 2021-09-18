import sys
sys.stdin = open('input_2439.txt', 'r')

# 백준 단계별 풀이 - for문 - 2439 문제
# 별을 찍되, 오른쪽 정렬시키기

N = int(input())
star = '*'
blank = ' '

for i in range(1, N+1):
    print((blank*(N-i)) + (star*i))
