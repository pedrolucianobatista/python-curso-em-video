# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
contribuicao = aposentadoria = 0
dados['nome'] = str(input('Nome: '))
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0: 
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    contribuicao = datetime.now().year - dados['contratação']
    dados['aposentadoria'] = (35 - contribuicao) + dados['idade']

print('-=' * 30)
print(dados)

for indice, valor in dados.items(): 
    print(f'{indice} tem o valor {valor}')
    