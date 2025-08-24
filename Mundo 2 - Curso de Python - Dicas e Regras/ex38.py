# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
# O primeiro valor é maior 
# O segundo valor é maior 
# Não existe valor maior, os dois são iguais 

cores = {
    'verde':'\033[32m',
    'azul':'\033[36m',
    'amarelo':'\033[33m',
    'normal':'\033[m'
}

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segunodo valor: '))

if a > b: 
    print(f"O maior é o {cores['verde']}PRIMEIRO{cores['normal']} valor")
elif b > a: 
    print(f"O maior é o {cores['azul']}SEGUNDO{cores['normal']} valor")
else: 
    print(f"Os dois valores são {cores['amarelo']}IGUAIS.{cores['normal']}")
    