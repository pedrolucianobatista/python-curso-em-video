# Crie um programa que leia dois números e mostre a soma entre eles. 

cores = {
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'normal':'\033[m'
}

valor1 = float(input('Digite o primeiro número: '))
valor2 = float(input('Digite o segundo número: '))

soma = valor1 + valor2

print("A soma entre {}{}{} e {}{}{} é igual a {}{:.2f}{}".format(cores['vermelho'], valor1, cores['normal'], cores['vermelho'], valor2, cores['normal'], cores['verde'], soma, cores['normal']))