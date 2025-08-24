# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 

from datetime import date

year = date.today().year
maior = 0
menor = 0

for count in range(1, 8): 
    data = int(input(f'Digite o ano do seu nascimento da {count}º pessoa: '))
    idade = year - data
    if idade >= 21: 
        maior += 1
    else: 
        menor += 1
        
print('Entre as sete pessoas, temos: ')
print(f'MAIORIDADE: {maior}')
print(f'MENORIDADE: {menor}')