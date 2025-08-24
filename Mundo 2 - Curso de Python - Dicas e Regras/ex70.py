# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: 
# A) Qual é o total gasto na compra. 
# B) Quantos produtos custam mais de R$1.000,00.
# C) Qual é o nome do produto mais barato. 

contador = total = menor = 0
titulo = 'LOJA SUPER BARATÃO'
fim = 'FIM DO PROGRAMA'

print(30 * '-')
print(titulo.center(30))
print(30 * '-')

nome = str(input('Nome do Produto: '))
preco = float(input('Preço: R$'))
resposta = str(input('Quer continuar? [S/N] '))
menor = preco
mProduto = nome 
total += preco

if resposta == 's':
    while True: 
        nome = str(input('Nome do Produto: '))
        preco = int(input('Preço: R$'))
        resposta = str(input('Quer continuar? [S/N] ')).lower()[0]
        total += preco
        if preco > 1000:
            contador += 1
        if preco < menor: 
            menor = preco
            mProduto = nome
        while resposta not in 'sn': 
            resposta = str(input('Quer continuar? [S/N] ')).lower()[0]
        if resposta == 'n': 
            break
        
print(30 * '-')
print(fim.center(30))
print(30 * '-')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {contador} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {mProduto} que custa R${menor:.2f}')