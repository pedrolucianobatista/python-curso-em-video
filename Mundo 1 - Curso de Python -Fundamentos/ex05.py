# Faça um programa que leia um número inteiro e mostre na tela o antecessor e o sucessor. 

cores = {
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'normal':'\033[m'
}

valor = int(input('Digite um número: '))

antecessor = valor - 1
sucessor = valor + 1

print("O sucessor do {}{}{} é igual a {}{}{}, e o antecessor é o {}{}{}".format(cores['vermelho'], valor, cores['normal'], cores['amarelo'], sucessor, cores['normal'], cores['verde'], antecessor, cores['normal']))