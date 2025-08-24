# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 

dicionario = {}

dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input('Média: '))
print("-=" * 20);

print(f'- nome é igual a {dicionario["nome"]}') 
print(f'- média é igual a {dicionario["media"]}')

if (dicionario['media'] > 6): 
    dicionario['situacao'] = 'Aprovado'
else: 
    dicionario['situacao'] = 'Reprovado'
    
print(f'- situação é igual a {dicionario["situacao"]}'); 
