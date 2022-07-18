L=[0]
for i in range(9):
    L.append(int(input()))

a = max(L)
b = L.index(a)

print(a)
print(b)