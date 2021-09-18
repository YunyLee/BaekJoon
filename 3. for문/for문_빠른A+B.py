import sys
sys.stdin = open('input_15552.txt', 'r')

# 백준 단계별 풀이 - for문 - 15552 문제
# 빠르게 입력받고 출력하는 문제

TC = int(sys.stdin.readline())
for test_case in range(TC):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# 시간을 줄이기 위해 input()보다 sys.stdin.readline()을 사용하자