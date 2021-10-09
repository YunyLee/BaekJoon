import sys
sys.stdin = open('input_14696.txt', 'r')

# A, B중 이기는 쪽, 무승부면 D

ROUND = int(input())
for test_case in range(1, ROUND+1):
    A_LIST = list(map(int,input().split()))
    B_LIST = list(map(int,input().split()))
    A = A_LIST.pop(0)
    B = B_LIST.pop(0)

    score = 4
    while True:
        if score == 0:
            print('D')
            break
        if score in A_LIST:
            if score in B_LIST:
                if A_LIST.count(score) == B_LIST.count(score):
                    score -= 1
                    continue
                elif A_LIST.count(score) > B_LIST.count(score):
                    print('A')
                    break
                else:
                    print('B')
                    break
            else:
                print('A')
                break
        elif score in B_LIST:
            if score in A_LIST:
                if A_LIST.count(score) == B_LIST.count(score):
                    score -= 1
                    continue
                elif A_LIST.count(score) > B_LIST.count(score):
                    print('A')
                    break
                else:
                    print('B')
                    break
            else:
                print('B')
                break
        else:
            score -= 1