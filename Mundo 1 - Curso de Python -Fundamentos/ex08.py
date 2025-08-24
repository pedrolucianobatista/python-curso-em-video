# Escreva um programa que leia um valor em metros e o exiba convertido na maior parte de conversões de medidas.

cores = {
    'azul':'\033[34m',
    'normal':'\033[m'
}

medida = float(input('Digite uma medida em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f"Km = {cores['azul']}{km}{cores['normal']}")
print(f"Hm = {cores['azul']}{hm}{cores['normal']}")
print(f"Dm = {cores['azul']}{dm}{cores['normal']}")
print(f"Dam = {cores['azul']}{dam}{cores['normal']}")
print(f"Cm = {cores['azul']}{cm}{cores['normal']}")
print(f"Mm = {cores['azul']}{mm}{cores['normal']}")
