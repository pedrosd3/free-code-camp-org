nomeCompleto = 'Pedro Ferreira'
nome = nomeCompleto[0:5]
sobrenome = nomeCompleto[6:]

print(nome)
print(sobrenome)

# ---------------------------------

vegetal = 'cenoura'
print('c' in vegetal)
print('i' in vegetal)

# ---------------------------------

teste = 'Bom Dia'
menor = teste.lower()
maior = teste.upper()

print(menor)
print(maior)

# ---------------------------------

cidade = 'florianopolis'
print(cidade.find('r'))
print(cidade.find('z'))

# ---------------------------------

cidade = 'mississipi'
cidadeNova = cidade.replace('s', 'z')

print(cidade)
print(cidadeNova)

# ---------------------------------

texto = ' | seu nome aqui | '

print(texto.lstrip())
print(texto.rstrip())
print(texto.strip())

# ---------------------------------

boasvindas = 'Seja bem-vindo ao nosso hotel'

print(boasvindas.startswith('Seja'))
print(boasvindas.startswith('seja'))

# ---------------------------------

email = 'Enviada por joao@gmail.com quinta-feira 15:49'

arroba = email.find('@')
final = email.find(' ', arroba)

print(email[arroba:final])