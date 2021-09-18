import sys
sys.stdin = open('input_2742.txt', 'r')

# 백준 단계별 풀이 - for문 - 2741 문제
# n부터 1까지 거꾸로 한줄에 하나씩 출력

N = int(input())

for i in range(N, 0, -1):
    print(i)