import sys
sys.stdin = open('input_11654.txt', 'r')

# 백준 - 단계별로 풀어보기 - 문자열 - 11654번 문제
# 주어진 글자의 아스키코드값을 출력하기

TC = 6

for test_case in range(1, TC+1):
    WORD = input()

    print(ord(WORD))