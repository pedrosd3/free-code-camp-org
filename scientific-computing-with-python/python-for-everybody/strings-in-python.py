nome = 'pedro'

for i in nome:
    print(i)
    
print(len(nome))

# -----------------

fruta = 'melancia'
cont = 0

while cont < len(fruta):
    letra = fruta[cont]
    print(cont, letra)
    cont += 1