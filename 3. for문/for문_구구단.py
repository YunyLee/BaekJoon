import sys
sys.stdin = open('input_2739.txt', 'r')

# 백준 단계별 풀이 - for문 - 2739 문제
# N 을 입력받고 구구단 N단을 출력하는 프로그램

N = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(N, i , N*i))

# range를 처음에 (10)이렇게 해서 틀렸었다.
# i가 1부터 시작해야되는것 간과하지말기!
