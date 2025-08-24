# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 

cores = {
    'vermelho':'\033[33;42m',
    'normal':'\033[m'
}

valor = int(input('Digite um valor: '))

print('-' * 12)
print(f"1  x {valor} = {cores['vermelho']}{valor * 1}{cores['normal']}")
print(f"2  x {valor} = {cores['vermelho']}{valor * 2}{cores['normal']}")
print(f"3  x {valor} = {cores['vermelho']}{valor * 3}{cores['normal']}")
print(f"4  x {valor} = {cores['vermelho']}{valor * 4}{cores['normal']}")
print(f"5  x {valor} = {cores['vermelho']}{valor * 5}{cores['normal']}")
print(f"6  x {valor} = {cores['vermelho']}{valor * 6}{cores['normal']}")
print(f"7  x {valor} = {cores['vermelho']}{valor * 7}{cores['normal']}")
print(f"8  x {valor} = {cores['vermelho']}{valor * 8}{cores['normal']}")
print(f"9  x {valor} = {cores['vermelho']}{valor * 9}{cores['normal']}")
print(f"10 x {valor} = {cores['vermelho']}{valor * 10}{cores['normal']}")
print('-' * 12)
