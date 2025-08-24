# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

temp = []
lista = []

while True: 
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N] '))[0].strip().lower()
    if resposta != 's' and resposta != 'n': 
        while True: 
            print('Resposta inválida!')
            resposta = str(input('Quer continuar? [S/N] '))[0].strip().lower()
            if resposta == 's' or resposta == 'n': 
                break
    if resposta == 'n': 
        break

print('-=' * 30)
print('No. NOME         MÉDIA')
print('-' * 25)

for i in range(0, len(lista)): 
    print(f'{i}   {lista[i][0]:12} {(lista[i][1] + lista[i][2]) / 2:.1f}')

print('-' * 35)

while True: 
    resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resposta == 999: 
        break
    if resposta < 0 or resposta >= len(lista): 
        while True: 
            print('Número do aluno inválido!')
            resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            if resposta == 999 or 0 <= resposta and resposta <= len(lista): 
                break
    if resposta == 999: 
        break
    print(f'Notas de {lista[resposta][0]} são [{lista[resposta][1]}, {lista[resposta][2]}]')
    print('-' * 35)

print('FINALIZANDO...')

sleep(1)

print('<<< VOLTE SEMPRE >>>')
