A = int(input())
B = int(input())
C = int(input())

D = A*B*C

L = len(str(D))
liszt = list(map(int,list(str(D))))

for i in range(0,10):
    Z = 0
    for j in range(L):
        if liszt[j]==i:
            Z+= 1
    print(Z)