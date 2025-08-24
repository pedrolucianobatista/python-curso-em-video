# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

cores = {
    'verde':'\033[32m',
    'normal':'\033[m', 
    'negrito':'\033[1m'
}

preco = float(input('Digite o valor do preço do produto: R$'))

desconto = preco * 0.95

print(f"Esse é o preço do valor do produto com 5% de desconto: {cores['negrito']}{cores['verde']}{desconto:.2f}R${cores['normal']}")
