from numpy import true_divide

soma = 0
for numeros in [12, 30, 8, 20]:
    soma = soma + numeros
    print(soma, numeros)
    
# ------------------------------

valor = False
print(valor)

for nums in [1, 2, 322, 4, 2]:
    if nums > 10:
        valor = True
    print(nums, valor)

print(valor)

# ------------------------------

menorNumero = None
print('começo',menorNumero)

for sequencia in [3, 22, 456, 88, -2]:
    if menorNumero is None:
        menorNumero = sequencia
    elif sequencia < menorNumero:
        menorNumero = sequencia
    print(menorNumero, sequencia)
    
print('fim', menorNumero)