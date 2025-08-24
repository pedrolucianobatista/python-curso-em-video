# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.                                              

termo = int(input('Digite o primeiro termo da progressão aritmétca: '))
razao = int(input('Digite a razão da progressão aritmética: '))

for count in range(0, 10):
    print(f'{termo + count * razao} ', end = '➡  ')

print('Finalizado!')
