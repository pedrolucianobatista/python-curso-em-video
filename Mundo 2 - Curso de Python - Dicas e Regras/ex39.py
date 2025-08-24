# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
# - Se ele ainda vai se alistar ao serviço militar. 
# - Se é a hora de se alistar. 
# Se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

from datetime import datetime

year = datetime.now().year
gen = str(input('Qual é o seu gênero? ').lower().strip())
idade = year - int(input('Em que ano você nasceu: '))

if gen == 'feminino':
    print('O seu alistamento não é obrigatório no Brasil!')
if idade == 18:
    print('Você está no ano de alistamento!')
    print(f"Deverá se alistar até o final de {year}")
elif idade > 18:
    print('Já se passou o ano do seu alistamento!')
if (idade - 18) > 1:
    print(f"Ele foi há {idade - 18} anos, e o ano foi de {year - (idade - 18)}")
elif (idade - 18) == 1: 
    print(f"Ele foi há 1 ano, e o ano foi de {year - (idade - 18)}")
elif idade < 18:
    print('Ainda vai chegar o ano do seu alistamento!')
if (18 - idade) > 1:
    print(f"Faltam {18 - idade} anos para o seu alistamento, e ele vai acontecer no ano de {year + (18 - idade)}")
elif (18 - idade) == 1: 
    print(f"Falta apenas 1 ano para o seu alistamento, e ele vai aconter no ao de {year + 1}")
