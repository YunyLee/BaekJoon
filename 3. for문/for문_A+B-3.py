import sys
sys.stdin = open('input_10950.txt', 'r')

# 백준 단계별 풀이 - for문 - 10950 문제
# A+B를 여러 번 출력하는 문제

def my_sum(a,b):
    return a+b

TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(int, input().split())
    result = my_sum(A,B)
    print(result)