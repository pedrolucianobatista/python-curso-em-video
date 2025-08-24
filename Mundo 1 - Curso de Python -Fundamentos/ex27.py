# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

cores = {
    'azul':'\033[36m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

nome = str(input('Digite o seu nome: '))

first = nome.split()[0]
words = nome.split().__len__()
last = nome.split()[words - 1]

print(f"Primeiro: {cores['azul']}{first}{cores['normal']}")
print(f"Último: {cores['vermelho']}{last}{cores['normal']}")
