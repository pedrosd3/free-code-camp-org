counts = dict()
print('Enter aline of text:')
line = input()

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# -------------------------------------------

animais = {'cachorro': 3, 'gato': 6, 'coelho': 8, 'tigre': 90}

for nome in animais:
    print(nome, animais[nome])
    
# -------------------------------------------

tabela = {'a': 1, 'b': 2, 'c': 3}

print(tabela.keys())
print(tabela.values())

# -------------------------------------------

aaa = {'jack': 2, 'bob': 4, 'henry': 8}

for bbb,ccc in aaa.items():
    print(bbb, ccc)