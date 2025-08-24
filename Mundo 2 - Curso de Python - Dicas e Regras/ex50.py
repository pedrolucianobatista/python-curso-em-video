# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for count in range(1, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        cont += 1
        soma += valor

print(f'Você digitou {cont} PARES, e a soma foi de {soma}!')
