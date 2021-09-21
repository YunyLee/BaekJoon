import sys
sys.stdin = open('input_2908.txt', 'r')

TC = 3

for test_case in range(1, TC+1):
    A, B = list(map(str,input().split()))

    a_list = []
    b_list = []

    for i in str(A):
        a_list.append(i)

    for i in str(B):
        b_list.append(i)

    result_a = ''
    result_b = ''
    for i in a_list[::-1]:
        result_a += i
    for i in b_list[::-1]:
        result_b += i

    print(max(int(result_a), int(result_b)))