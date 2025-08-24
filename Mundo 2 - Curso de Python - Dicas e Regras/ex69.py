# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) Quantas pessoas tem mais de 18 anos. 
# B) Quantos homens foram cadastrados. 
# C) Quantas mulheres tem menos de 20 anos. 

maior = homens = mulheres = 0
cadastro = 'CADASTRE UMA PESSOA'

while True: 
    print('-' * 30)
    print(cadastro.center(30))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = (input('Sexo: [M/F] ').lower().strip())
    while sexo != 'm' and sexo != 'f': 
        sexo = (input('Sexo: [M/F] '))
    resposta = (input('Quer continuar? [S/N] ').lower().strip())
    while resposta != 's' and resposta != 'n': 
        resposta = (input('Quer continuar? [S/N] ').lower().strip())
    if idade > 18: 
        maior += 1
    if sexo == 'm': 
        homens += 1
    if sexo == 'f' and idade < 20: 
        mulheres += 1  
    if resposta != 's': 
        break
    
print(f'Maiores: {maior} pessoas')
print(f'Homens: {homens} pessoas')
print(f'Mulheres menores de 20 anos: {mulheres} pessoas')
