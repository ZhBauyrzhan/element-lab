def pow(a: float, n: int):
    return a ** n


a = input().split()
print(pow(float(a[0]), int(a[1])))
