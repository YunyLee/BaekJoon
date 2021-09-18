import sys
sys.stdin = open('input_14681.txt', 'r')

# 백준 단계별 풀이 - if문 - 14681 문제
# 주어진 점이 어느 사분면에 속하는지 알아내기

X = int(input())
Y = int(input())

if X>0 and Y>0:
    print(1)
elif X>0 and Y<0:
    print(4)
elif X<0 and Y>0:
    print(2)
else:
    print(3)