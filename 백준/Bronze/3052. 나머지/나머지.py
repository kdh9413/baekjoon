liszt = []
for i in range(10):
    liszt.append(int(input())%42)

liszt2 = []
for i in liszt:
    if i not in liszt2:
        liszt2.append(i)

z = len(liszt2)
print(z)
