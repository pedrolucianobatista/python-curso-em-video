# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

cores = {
    'amarelo':'\033[33m',
    'normal':'\033[m'
}

variavel = (input('Digite algo: '))

print("O tipo primitivo desse valor é {}{}{}".format(cores['amarelo'], type(variavel), cores['normal']))
print("Só tem espaços? {}{}{}".format(cores['amarelo'], variavel.isspace(), cores['normal']))
print("É um número {}{}{}".format(cores['amarelo'], variavel.isnumeric(), cores['normal']))
print("É alfabético? {}{}{}".format(cores['amarelo'], variavel.isalpha(), cores['normal']))
print("É alfanumérico? {}{}{}".format(cores['amarelo'], variavel.isalnum(), cores['normal']))
print("Está em maiúsculas? {}{}{}".format(cores['amarelo'], variavel.isupper(), cores['normal']))
print("Está em minúsculas? {}{}{}".format(cores['amarelo'], variavel.islower(), cores['normal']))
print("Está capitalizada? {}{}{}".format(cores['amarelo'], variavel.istitle(), cores['normal']))
