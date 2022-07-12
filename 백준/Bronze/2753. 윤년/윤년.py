P = int(input())


if (P%4 == 0 and P%100 != 0) or P%400 == 0 :
    print('1')

else:
    print('0')