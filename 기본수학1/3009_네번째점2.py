import sys
sys.stdin = open('input_3009.txt', 'r')

x = []
y = []

for i in range(3):
    X, Y = map(int,input().split())

    x.append(X)
    y.append(Y)

a = b = 0
for i in range(len(x)):
    if x.count(x[i]) == 1:
        a = x[i]
    if y.count(y[i]) == 1:
        b = y[i]

print(a,b)