import sys
sys.stdin = open('input_4344.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):

    N_LIST = list(map(int,input().split()))
    N = N_LIST[0]
    del N_LIST[0]

    score_average = sum(N_LIST)/N
    cnt = 0

    for i in N_LIST:
        if i > score_average:
            cnt += 1

    result = (cnt/N) * 100
    print('{0:0.3f}%'.format(result))
    # {0.03f}로 소수점 3째자리까지 출력가능!!
