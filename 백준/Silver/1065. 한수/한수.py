a = int(input()) + 1
y = []

for k in range(1,a):
    c = len(str(k)) - 1
    x = set()
    for i in range(c):
        j = i+1
        d = int(str(k)[j])-int(str(k)[i])
        x.add(d)
        
    if len(x) <= 1:
        y.append(k)

z = len(y)
print(z)     
     