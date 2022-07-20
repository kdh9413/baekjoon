a = []

for i in range(2,10001):
    e = 0
    if i > 1:
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                e += 1
                break
        if e == 0:
            a.append(i)


T = int(input())

for i in range(T):
    n = int(input())
    n2 = int(n/2)
    n3 = n2
    while True:
        if n2 in a and n3 in a:
            break
        else:
            n2 -= 1
            n3 += 1
    print(n2,n3,sep=' ')
