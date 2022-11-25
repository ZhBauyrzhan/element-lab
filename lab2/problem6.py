def pow(a: float, n: int):
    return a ** n


a, n = map(float, input().split())
print(pow(float(a), int(n)))
