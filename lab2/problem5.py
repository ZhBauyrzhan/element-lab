bi = input()
dec = 0
for index, val in enumerate(bi):
    dec+=(int(val) * 2**(len(bi)-index-1))
print(dec)