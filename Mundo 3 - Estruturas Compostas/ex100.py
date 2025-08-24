# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior. 

import random 
from time import sleep

numeros = list(); 

def sortear(lista): 
    print('Sorteando 5 valores da lista: ', end='')

    for i in range(0, 5): 
        lista.append(random.randint(1, 10))
        print(f'{lista[i]}', end = ' ', flush=True)
        sleep(0.5)
    print(' PRONTO!')

def somaPar(lista): 
    soma = 0; 
    for i in range(0, len(lista)): 
        if (lista[i] % 2 == 0): 
            soma += lista[i]
    print(f'Somando os valores pares de {lista}, temos {soma}')

sortear(numeros)
somaPar(numeros)
