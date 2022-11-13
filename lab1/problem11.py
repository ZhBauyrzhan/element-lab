a = int(input())
b = int(input())
c = int(input())
if a > b:
    d = b
    b = a
    a = d
if b > c:
    d = c
    c = b
    b = d
if a > b:
    d = b
    b = a
    a = d
if a >= b+c or b >= a+c or c >= a+b:
    print('impossible')
elif a**2 + b**2 == c**2:
    print('right')
elif a**2 + b**2 > c**2:
    print('acute')
else:
    print('obtuse')