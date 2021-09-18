import sys
sys.stdin = open('input_11022.txt', 'r')

# 백준 단계별 풀이 - for문 - 11022 문제
# 좀 더 촐력 예쁘게

TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(int, input().split())
    result = A+B
    print('Case #{}: {} + {} = {}'.format(test_case, A, B, result))
