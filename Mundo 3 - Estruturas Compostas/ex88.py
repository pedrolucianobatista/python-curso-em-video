# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 

from random import randint
from time import sleep

temp = []
sorteado = 0
lista = []

print('-' * 30)

titulo = 'JOGA NA MEGA SENA'

print(f'{titulo:^30}')
print('-' * 30)

vezes = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 5, f'SORTEANDO {vezes} JOGOS', '-=' * 5)

for i in range(0, vezes): 
    for j in range(0, 6): 
        sorteado = randint(1, 60)
        if sorteado is not temp: 
            temp.append(sorteado)
    temp.sort()
    lista.append(temp[:])
    temp.clear()

for i in range(0, vezes): 
    sleep(1)
    print(f'Jogo {i + 1}: {lista[i]}')

print('-=' * 5, f' < BOA SORTE! > ', '-=' * 5)
