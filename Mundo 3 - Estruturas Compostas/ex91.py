# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep

valores = []
valorestemp = {}
aux = 0

print('Valores sorteados: ')

for i in range(0, 4): 
    valorestemp['jogador'] = (f'jogador{i + 1}')
    valorestemp['valor'] = randint(1, 6)
    valores.append(valorestemp.copy())
    sleep(1)
    print(f'O {valores[i]['jogador']} tirou {valores[i]['valor']}')

print('Ranking dos jogadores: ')

for i in range(0, len(valores)): 
    for j in range(i, len(valores)): 
        if valores[i]['valor'] < valores[j]['valor']: 
            aux = valores[i]['valor']
            valores[i]['valor'] = valores[j]['valor']
            valores[j]['valor'] = aux

for i in range(0, len(valores)): 
    sleep(1)
    print(f'{i + 1}º lugar: {valores[i]['jogador']} com {valores[i]['valor']}')
