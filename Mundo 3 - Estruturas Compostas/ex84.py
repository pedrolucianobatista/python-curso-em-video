# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

lista1 = list()
lista = list()
maior = menor = 0

while True: 
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    lista.append(lista1[:])
    lista1.clear()
    resposta = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resposta != 's' and resposta != 'n': 
        print('resposta errada!')
        while True: 
            resposta = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
            if resposta == 's' or resposta == 'n': 
                break
    if resposta == 'n': 
        break

for i in range(0, len(lista)): 
    if i == 0: 
        menor = lista[i][1]
    elif lista[i][1] < menor: 
        menor = lista[i][1]
    if lista[i][1] > maior: 
        maior = lista[i][1]

print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end = '')

for i in range(0, len(lista)): 
    if lista[i][1] == maior: 
        print(f'[{lista[i][0]}]', end = ' ')

print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end = '')

for i in range(0, len(lista)): 
    if lista[i][1] == menor: 
        print(f'[{lista[i][0]}]', end = ' ')
