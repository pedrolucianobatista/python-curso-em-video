# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m', 
    'normal':'\033[m'
}

print('-=-' * 10)
print('Analisador de Triângulos')

print('-=-' * 10)
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
print('-=-' * 10)

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print(f"{cores['verde']}É um TRIÂNGULO!{cores['normal']}")   
else: 
    print(f"{cores['vermelho']}Não é um TRIÂNGULO!{cores['normal']}")
