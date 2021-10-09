import sys
sys.stdin = open('input_13300.txt', 'r')

# 13300 방배정

N, K = map(int,input().split())
girls_dict = dict()
boys_dict = dict()
cnt = 0

for i in range(N):
    GENDER, GRADES = map(int,input().split())

    if GENDER == 0:
        if GRADES not in boys_dict.keys():
           boys_dict[GRADES] = 1
        else:
            boys_dict[GRADES] += 1
    elif GENDER == 1:
        if GRADES not in girls_dict.keys():
           girls_dict[GRADES] = 1
        else:
            girls_dict[GRADES] += 1

for i in boys_dict.keys():
    if boys_dict[i] <=K:
        cnt += 1
    else:
        if boys_dict[i] % K == 0:
            cnt += boys_dict[i] // K
        else:
            cnt += (boys_dict[i] // K) +1

for i in girls_dict.keys():
    if girls_dict[i] <=K:
        cnt += 1
    else:
        if girls_dict[i] % K == 0:
            cnt += girls_dict[i] // K
        else:
            cnt += (girls_dict[i] // K) +1

print(cnt)
