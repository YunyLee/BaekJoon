import sys
sys.stdin = open('input_2675.txt', 'r')

# 백준 - 단계별로 풀어보기 - 문자열 - 2675번 문제

TC = int(input())

for test_case in range(1, TC+1):
    R, S = map(str, input().split())

    for i in S:
        print(i * int(R), end='')
    print()