nome = 'pedro'

if nome == 'carlos':
    print("o nome é carlos")
elif nome == 'julio':
    print("o nome é julio")
elif nome == 'pedro':
    print("o nome é pedro")
else:
    print("nome não encontrado")
    
# --------------------------------

geb = 'hello everyone!'
try:
    wer = int(geb)
except:
    wer = -1 
print('o valor de wer é', wer)

xml = '233'
try:
    xtt = int(xml)
except:
    xtt = -1 
print('o valor de xtt é', xtt)

# --------------------------------

aqui = input("Digite um número:")
try:
    result = int(aqui)
except:
    result = -1
    
if result >= 0:
    print("Muito bem")
else:
    print("Input não é um número")