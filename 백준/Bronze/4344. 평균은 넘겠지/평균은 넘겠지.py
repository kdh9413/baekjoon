C = int(input())

for i in range(C):
    liszt = list(map(int,input().split()))
    a = sum(liszt[1:]) #총점수
    n = liszt[0] #학생수
    b = a/n #평균
    c = 0
    for j in range(1,n+1):
        if liszt[j] > b:
            c+= 1
    zz = round(c/n*100,3)
    z = f'{zz:.3f}%'
    print(z)

