# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import datetime

idade = datetime.now().year - int(input('Digite o ano do seu nascimento: '))

if idade == 1: 
    print(f"O atleta tem {idade} ano.")
else: 
    print(f"O atleta tem {idade} anos.")
if 9 >= idade:
    print('Classificação: MIRIM')
elif 14 >= idade: 
    print('Classificação: INFANTIL')
elif 19 >= idade: 
    print('Classificação: JÚNIOR')
elif 20 >= idade: 
    print('Classificação: SÊNIOR')
else: 
    print('Classificação: MASTER')
