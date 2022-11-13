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
print(a, b, c)
