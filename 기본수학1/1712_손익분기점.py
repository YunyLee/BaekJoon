import sys
sys.stdin = open('input_1712.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    A, B, C = map(int,input().split())
    result = -1 # 손익분기점이 존재하지 않으면 -1을 출력하게끔

    if C-B > 0: # 분모
        result = int(A/(C-B))+1

    print(result)