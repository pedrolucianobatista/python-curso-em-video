# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO ou não. 

from datetime import datetime 

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

date = datetime.now()
year = date.year
ano = int(input('Digite o ano: '))

if ano <= 0:
    print("O ano atual é {}".format(year))
elif ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano {ano} {cores['verde']}é BISSEXTO!{cores['normal']}")
else: 
    print(f"O ano {ano} {cores['vermelho']}não é BISSEXTO!{cores['normal']}")
