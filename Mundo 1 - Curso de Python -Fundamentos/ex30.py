# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. 

cores = {
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'normal':'\033[m'
}

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f"O número {num} é {cores['verde']}PAR{cores['normal']}")
else: 
    print(f"O número {num} é {cores['amarelo']}ÍMPAR{cores['normal']}")
