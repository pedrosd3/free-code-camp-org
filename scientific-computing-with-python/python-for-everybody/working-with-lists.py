a = [33, 67, 2, 11]
b = [13, 9, 3, 890]

c = a + b
print(c)

# ------------------------------

wer = [12, 45, 56, 89, 23, 73]
print(wer[2:])
print(wer[:3])
print(wer[1:4])

# ------------------------------

x = list()
print(dir(x))

# ------------------------------

stuff = []
stuff.append(2)
stuff.append(54)
stuff.append(88)

print(stuff)

# ------------------------------

biglist = [2, 4, 66, 55, 88, 8776, 3, 4, 90, 707]

if 2 in biglist:
    print(True)
else:
    print(False)
    
if 433 not in biglist:
    print(True)
else:
    print(False)
    
# ------------------------------

ordem = [44, 76, 7, 2,  9999, 10]
ordem.sort()

print(ordem)
print(sum(ordem))