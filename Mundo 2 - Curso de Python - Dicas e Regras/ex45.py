# Crie um programa que faça o computador jogar Jokenpô com você. 

from time import sleep
from random import choice

cores = {
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'normal':'\033[m'
}

print(f"{'JOKENPÔ':=^40}")
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('\nQual é a sua opção escolhida? '))
print('=' * 40)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

opcoes = ['pedra', 'papel', 'tesoura']
sorteado = choice(opcoes)
array = ['pedra', 'papel', 'tesoura']

if opcao > 3 or opcao <= 0:
    print(f"{cores['vermelho']}OPÇÃO INVÁLIDA!{cores['normal']}")
else: 
    print(f"USER: {array[opcao - 1]}")
    print(f"COMPUTER: {sorteado}")
    if opcao == 1 and sorteado == 'papel' or opcao == 2 and sorteado == 'tesoura' or opcao == 3 and sorteado == 'pedra':
        print(f"{cores['vermelho']}VOCÊ PERDEU!{cores['normal']}")
    elif array[opcao - 1] == sorteado: 
        print(f"{cores['amarelo']}EMPATE!{cores['normal']}")
    else: 
        print(f"{cores['verde']}VOCÊ GANHOU!{cores['normal']}")
