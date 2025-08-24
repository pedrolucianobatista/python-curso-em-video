# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. 

head = 'BANCO CEV'

print(30 * '=')
print(head.center(30))
print(30 * '=')

while True: 
    valor = int(input('Que valor você quer sacar? R$'))
    resto = valor
    div50 = (valor / 50).__floor__()
    if div50 > 0: 
        print(f'Total de {div50} cédulas de R$50,00')    
        resto = resto - div50 * 50
    div20 = (resto / 20).__floor__()
    if div20 > 0: 
        print(f'Total de {div20} cédulas de R$20,00')
        resto = resto - div20 * 20
    div10 = (resto / 10).__floor__()
    if div10 > 0: 
        print(f'Total de {div10} cédulas de R$10,00')
        resto = resto - div10 * 10
    div5 = (resto / 5).__floor__()
    if div5 > 0: 
        print(f'Total de {div5} cédulas de R$5,00')
        resto = resto - div5 * 5
    div1 = (resto / 1).__floor__()
    if div1 > 0: 
        print(f'Total de {div1} cédulas de R$1,00')
    break

print(30 * '=')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')