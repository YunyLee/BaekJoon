import sys
sys.stdin = open('input_1152.txt', 'r')

TC = 3

for test_case in range(1, TC+1):

    SENTENCE = input().split()
    print(len(SENTENCE))
    # print(SENTENCE.count(' ')+1)
