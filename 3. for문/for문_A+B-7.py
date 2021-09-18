import sys
sys.stdin = open('input_11021.txt', 'r')

# 백준 단계별 풀이 - for문 - 11021 문제
# A+B를 출력하는 프로그램
TC = int(input())
for test_case in range(1, TC+1):
    A, B = map(int, input().split())
    result = A+B
    print('Case #{}: {}'.format(test_case, result))