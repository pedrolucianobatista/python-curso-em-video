# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

cores = {
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'azul':'\033[36m',
    'normal':'\033[m'
}

angulo = int(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"Esse é o seno {cores['amarelo']}{seno:.2f}{cores['normal']}")
print(f"Esse é o cosseno {cores['vermelho']}{cosseno:.2f}{cores['normal']}")
print(f"Esse é a tangente {cores['azul']}{tangente:.2f}{cores['normal']}") 
