lista = ['pedro', 'andré', 'marcos', 'lucas', 'paulo']

lista[2] = 'paloma'

for amigo in lista:
    if amigo[0] == 'p':
        print(amigo)

print('-------')
     
for i in range(len(lista)):
    item = lista[i]
    print(item)