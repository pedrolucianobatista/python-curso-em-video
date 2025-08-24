# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
# Condição de existência de um número primo: Divisível por 1 e por ele mesmo apenas. Obs: O número 1 não é!

contador = 0

value = int(input('Digite um número: '))

for count in range(1, value + 1): 
    if value % count == 0:
        contador += 1
        print(f'\033[33m', end = ' ')
    else: 
        print(f'\033[31m', end = ' ')
    print(f'{count}\033[m', end = ' ')

if contador == 1: 
    print(f'\nO número {value} foi divisível por 1 vez')
else: 
    print(f'\nO número {value} foi divisível por {contador} vezes')
    
if contador == 2: 
    print('E por isso ele é PRIMO!')
else: 
    print('E por isso ele NÃO É PRIMO!')
