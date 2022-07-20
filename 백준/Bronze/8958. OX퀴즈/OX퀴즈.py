n = int(input())

for i in range(n):
    liszt = []
    z = 0
    word = input()
    liszt = word.split('X')
    for j in range(len(liszt)):
        a = len(liszt[j])
        b = round(a*(1+a)/2)
        z+= b
    print(z)