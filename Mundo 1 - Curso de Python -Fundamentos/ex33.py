# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.  

cores = {
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'agua':'\033[36m',
    'normal':'\033[m'
}

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

menor = valor1

if menor > valor2 and valor2 < valor3:
    menor = valor2
if menor > valor3 and valor3 < valor2:
    menor = valor3

print(f"Esse foi o menor valor digitado {cores['azul']}{menor:.0f}{cores['normal']}")

maior = valor1

if maior < valor2 and valor2 > valor3:
    maior = valor2
if maior < valor3 and valor3 > valor2:
    maior = valor3

print(f"Esse foi o maior valor digitado {cores['roxo']}{maior:.0f}{cores['normal']}")
