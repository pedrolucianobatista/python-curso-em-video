# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

from math import hypot

cores = {
    'azul':'\033[34m',
    'normal':'\033[m'
}

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(co, ca)

print(f"A hipotenusa vai medir {cores['azul']}{hi:.2f}{cores['normal']}")