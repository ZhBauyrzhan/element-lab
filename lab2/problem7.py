def election(x: bool, y: bool, z: bool):
    count = 0
    if x:
        count += 1
    if y:
        count += 1
    if z:
        count += 1
    # print(count)
    return 1 if count >= 2 else 0


x, y, z = map(int, input().split())
# print(x, y, z)
print(election(x, y, z))
