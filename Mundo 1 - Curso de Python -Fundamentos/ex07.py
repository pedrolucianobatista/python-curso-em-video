# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. 

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 5: 
    print(f"A média das notas do aluno é de {cores['verde']}{media}{cores['normal']}")
else: 
    print(f"A média das notas do aluno é de {cores['vermelho']}{media}{cores['normal']}")
