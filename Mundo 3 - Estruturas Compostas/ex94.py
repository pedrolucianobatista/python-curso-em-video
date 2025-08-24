# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade do grupo. 
# C) Uma lista com todas as mulheres. 
# D) Uma lista com todas as pessoas com idade acima da média. 
# Usar a paradinha do copy acredito eu
# Usar a verificação da resposta apenas no final do código

temp = {} 
dados = []
media = 0

while True: 
    temp['nome'] = str(input('Nome: '))
    temp['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    temp['idade'] = int(input('Idade: '))
    resposta = str(input('Quer continuar? [S/N] '))[0].lower()
    media += temp['idade']
    dados.append(temp.copy())
    if 'n' in resposta: 
        break

print('-=' * 30)
print(f'- O grupo tem {len(dados)} pessoas.')
print(f'- A média de idade é de {media / len(dados):.2f}')
print(f'- As mulheres cadastradas foram: ', end = '')

for i in range(0, len(dados)): 
    if dados[i]['sexo'] == 'F': 
        print(f'{dados[i]['nome']}', end = ' ')

print(f'\n- Lista das pessoas que estão acima da média: ')

for i in range(0, len(dados)): 
    if dados[i]['idade'] > (media / len(dados)): 
        print()
        print(f'nome = {dados[i]['nome']}; sexo = {dados[i]['sexo']}; idade = {dados[i]['idade']};')

print('<< ENCERRADO >>')
