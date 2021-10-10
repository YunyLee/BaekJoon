import sys
sys.stdin = open('input_2869.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    A, B, V = map(int,input().split())

    V -= B # 마지막날은 미끄러지지않으니까

    if V%(A-B) != 0:
        cnt = (V//(A-B)) +1
    else:
        cnt = (V//(A-B))

    print(cnt)