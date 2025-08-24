# Crie um programa que leia o nome completo de uma pessoa e mostre: 

# * O nome com todas as letras maiúsculas e minúsculas. 
# * Quantas letras ao todo (sem considerar espaços).
# * Quantas letras tem o primeiro nome. 

cores = {
    'verde':'\033[32m', 
    'normal':'\033[m'
}

nome = str(input('Qual o seu nome: '))

print(f"O seu nome completo tem {cores['verde']}{nome.replace(' ','').__len__()} letras{cores['normal']}")
print(f"O seu nome em maiúsculo é: {cores['verde']}{nome.upper()}{cores['normal']}")
print(f"O seu nome em minúsculo é: {cores['verde']}{nome.lower()}{cores['normal']}")
print(f"O seu primeiro nome tem {cores['verde']}{nome.split()[0].__len__()} letras{cores['normal']}")
