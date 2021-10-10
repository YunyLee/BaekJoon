import sys
sys.stdin = open('input_3009.txt', 'r')

# 3009 네번째 점 fail
temp = []
temp2 = []
for i in range(3): # 점이 3개니까 3
    A, B = map(int,input().split())
    result = []
    result2 = ''

    if A not in temp:
        temp.append(A)
        temp2.append(A)
    else:
        temp.pop(temp.index(A))
        temp2.append(A)
    if B not in temp:
        temp.append(B)
        temp2.append(B)
    else:
        temp.pop(temp.index(B))
        temp2.append(B)

if len(temp) == 0:
    for j in range(len(temp2)):
        print(temp2)
        if temp2.count(temp2[j]) == 4:
            result = temp2
            result.remove(temp2[j])
            result.remove(temp2[j])
            result.remove(temp2[j])
            result.remove(temp2[j])
            for i in result:
                result2 += str(i) + ' '
        print(result2)
elif len(temp) != 0:
    for i in temp:
        result2 += str(i) + ' '
    print(result2)
