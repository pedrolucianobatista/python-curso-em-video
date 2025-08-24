# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. 

cores = {
    'azul':'\033[34m',
    'normal':'\033[m',
    'azulSublinhado':'\033[4;34m',
    'negritoAzul':'\033[1;35m'
}

nome = input('Qual é o seu nome: ').strip()

print("Muito prazer, {}{}!{} Seja bem-vindo(a)".format(cores['negritoAzul'], nome, cores['normal']))
