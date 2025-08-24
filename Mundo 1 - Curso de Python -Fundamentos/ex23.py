# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

# Ex: 
# Digite um número: 1834
# Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

cores = {
    'azul':'\033[36m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'normal':'\033[m'
}

valor = int(input('Digite um número: '))

milhar = int(valor / 1000)
centena = int(valor / 100) % 10
dezena = int(valor / 10) % 10
unidade = valor % 10

print(f"{cores['azul']}Unidade: {unidade}{cores['normal']}\n{cores['vermelho']}Dezena: {dezena}{cores['normal']}\n{cores['verde']}Centena: {centena}{cores['normal']}\n{cores['amarelo']}Milhar: {milhar}{cores['normal']}")
