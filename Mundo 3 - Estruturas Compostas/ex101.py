# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. 

def voto(anoNasc): 
    from datetime import datetime

    idade = datetime.now().year - anoNasc

    if (idade >= 18 and idade <= 70): 
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif (16 <= idade >= 17 and idade > 70): 
        return f'Com {idade} anos: VOTO OPCIONAL'
    else: 
        return f'Com {idade} anos: NÃO VOTA'

print('-' * 30)
ano = int(input('Ano de nascimento: '))

print(voto(ano))
