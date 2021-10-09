import sys
sys.stdin = open('input_2309.txt', 'r')

N = []
for i in range(9):
    temp = int(input())
    N.append(temp)

N = sorted(N) # 정렬하기

total_sum = sum(N)
sumV = 100

goal = total_sum - sumV # 여기서는 40
remove1 = 0
remove2 = 0

for i in range(len(N)):
    for j in range(len(N)):
        if N[i] + N[j] == goal:
            remove1 = N[i]
            remove2 = N[j]
            break

N.remove(remove1)
N.remove(remove2)

for k in N:
    print(k)
