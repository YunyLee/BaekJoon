import sys
sys.stdin = open('input_5622.txt', 'r')

TC = 2

for test_case in range(1, TC+1):
    A = input()
    min_time = 0

    alphabet = ['-','-','1','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    for j in A:
        for i in alphabet:
            if j in i:
                min_time += alphabet.index(i)

    print(min_time)

    arr = [0]*10
    print(arr)