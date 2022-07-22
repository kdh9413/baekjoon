a = set(range(1,10001))
b = set()

def f(x):
    for i in str(x):
        x += int(i)
    return(x)

for i in range(1,10001):
    b.add(f(i))


z = sorted(a - b)

for i in z:
    print(i)