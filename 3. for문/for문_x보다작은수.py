import sys
sys.stdin = open('input_10871.txt', 'r')

# 백준 단계별 풀이 - for문 - 10871 문제
# A에서 X보다 작은 수를 모두 출력하기

N, X = map(int, input().split())
A = list(map(int,input().split()))

for i in A:
    if i < X:
        print(i, end =' ')