A = int(input())
n = 0
Z = A

while True:
    Z = 10*(Z%10)+(Z//10+Z%10)%10
    n+= 1
    if Z==A:
        print(n)
        break