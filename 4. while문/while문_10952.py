import sys
sys.stdin = open('input_10952.txt', 'r')

# 백준 단계별 풀이 - while문 - 10952문제
# 0 0이 들어올 때까지 A+B를 출력하는 문제

NUM1 = 1
NUM2 = 1

while NUM1 != 0 and NUM2 != 0:
    NUM1, NUM2 = map(int, input().split())
    if NUM1 !=0 and NUM2 !=0:
        print(NUM1 + NUM2)
