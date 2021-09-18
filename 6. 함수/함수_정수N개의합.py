# 백준 단계별 풀이 - 함수 - 15596 문제
# n개의 합을 구하는 함수

# def solve(a):
#     return sum(a) 간단하게 sum함수 이용하기

def solve(a):
    total = 0
    for i in a:
        total += i
    return total