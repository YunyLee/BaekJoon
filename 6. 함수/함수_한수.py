import sys
sys.stdin = open('input_1065.txt', 'r')

# 백준 단계별 풀이 - 함수 - 1065 문제
# 한수를 찾아서 개수를 출력하는 문제

def hansu(num) :
    hansu = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu += 1  # 100보다 작으면 모두 한수 (차이가 1로 일정하기 때문)
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu += 1  # 각 자리가 등차수열이면 한수
    return hansu

N= int(input())
print(hansu(N))