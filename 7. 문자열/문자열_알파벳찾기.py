import sys
sys.stdin = open('input_10809.txt', 'r')

# 백준 - 단계별로 풀어보기 - 문자열 - 11720번 문제
# 단어의 위치를 출력하자 없으면 -1

S = input()

# 방법1 index활용
'''
for i in range(97,123):
    if chr(i) in S:
        print(S.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
'''
# 방법2 for else구문 활용
'''
for i in range(97,123):
    for j in range(len(S)):
        if chr(i) == S[j]:
            print(j, end=' ')
            break #가장가까운 for루프 빠져나감
    else: #break로 빠져나가지 않고 다 돈 경우
        print(-1, end=' ')
'''
# 인덱스 찾는 함수 활용하기

def myindex(v):
    for i in range(97,123):
        for j in range(len(v)):
            if chr(i) == v[j]:
                print(j, end=' ')
                break
        else:
            print(-1, end=' ')

myindex(S)

# 가장 중요한 포인트! for else 구문 사용시 break를 잊지말기!