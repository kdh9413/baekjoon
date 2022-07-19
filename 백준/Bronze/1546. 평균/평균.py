N = int(input())
liszt = list(map(int,input().split()))
b = 0

for i in liszt:
    a = i/max(liszt)*100
    b+= a

z=b/N

print(z)
