# Crie um programa que leia o nomde de uma pessoa e diga se ela tem "SILVA" no nome. 

cores = {
    'verde':'\033[32m', 
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

nome = str(input('Digite o seu nome completo: ').lower().strip())

find = nome.find('silva')

if find > -1:
    print(f"{cores["verde"]}True{cores["normal"]}")
else:
    print(f"{cores['vermelho']}False{cores['normal']}")
