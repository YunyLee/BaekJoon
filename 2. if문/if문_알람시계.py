import sys
sys.stdin = open('input_2884.txt', 'r')

# 백준 단계별 풀이 - if문 - 2884 문제
# 시간 뺄셈 문제 (45분 일찍 알람 설정하기 문제)

H, M = map(int, input().split())

M -= 45

if M<0:
    M += 60 # 음수가 되면 60을 더해주고 그만큼 H에서 1을 빼주자
    if H==0:
        H = 23
    elif H!=0:
        H -= 1
print(H,M)
