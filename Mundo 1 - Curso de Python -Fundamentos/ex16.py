# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. 

from math import trunc

cores = {
    'preto':'\033[37;47m',
    'normal':'\033[m'
}

valor = float(input('Digite um número: '))

print(f"O número {valor} tem a parte inteira {cores['preto']}{trunc(valor)}{cores['normal']}")