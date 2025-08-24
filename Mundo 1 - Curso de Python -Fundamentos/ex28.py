# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
from time import sleep

cores = {
    'verde':'\033[32m', 
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
    'azul':'\033[36m',
    'normal':'\033[m'
}

print(f"{cores['amarelo']}-=-{cores['normal']}" * 20)
print(f"{cores['amarelo']}Vou pensar em um número entre 0 e 5. Tente advinhar...{cores['normal']}")
print(f"{cores['amarelo']}-=-{cores['normal']}" * 20)

num = int(input('Digite um número para acertar: '))
ran = randint(0, 5)

print(f"{cores['azul']}PROCESSANDO...{cores['normal']}")
sleep(1.5)

if num == ran:
    print(f"{cores['verde']}Parabéns! Você acertou, o número sorteado foi o {ran}{cores['normal']}")
else:
    print(f"{cores['vermelho']}Errou! O número sorteado foi o {ran}{cores['normal']}")
