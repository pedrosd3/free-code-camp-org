txt = {'abc': 3, 'wwe': 5, 'top':2, 'spc': 99, 'xyz': 1}
print('ABC' in txt)
cont = 0

for i in txt:
    if cont < txt[i]:
        cont = txt[i]
    
print(cont)

print(txt.get('abc', 345))