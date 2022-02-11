def soma(a, b):
    print(a + b)
    
soma(3, 5)
soma(9, 0)
soma(67309867, 33)

# ------------------

def ola(lingua):
    if lingua == 'pt-br':
        print("olá")
    elif lingua == 'en':
        print("hi")
    elif lingua == 'es':
        print("hola")
    else:
        print("lingua não suportada")
        
ola('pt-br')
ola('russo')

# ------------------

def greet():
    return 'Hello'

print(greet(), 'my friends')
print(greet(), 'everyone')