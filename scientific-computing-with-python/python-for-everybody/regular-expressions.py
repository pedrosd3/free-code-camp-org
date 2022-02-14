import re

texto = open('ideis.txt')

for linha in texto:
    linha = linha.rstrip()
    if re.search('^M', linha):
        print(linha)