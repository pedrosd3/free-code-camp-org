x = open('teste.txt')
count = 0

for i in x:
    count += 1
    print('contagem de linhas', count)

# --------------------------------------

y = open('teste.txt')

for item in y:
    item = item.rstrip()
    if item.startswith('Lorem'):
        print(item)
        
# --------------------------------------

z = open("ideis.txt")

for word in z:
    word = word.rstrip()
    if not 'are' in word:
        continue
    print(word)
    
# --------------------------------------

nomeArquivo = input("digite o nome do arquivo: ")
try:
    arquivo = open(nomeArquivo)
except:
    print("O arquivo", nomeArquivo, "não foi encontrado")
    quit()

cont = 0

for linhas in arquivo:
    cont += 1
print(nomeArquivo, "possui", cont, "linhas.")