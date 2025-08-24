# Faça um programa que calcule a soma entre todos números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500. 

soma = 0
valores = 0

for count in range(1, 500, 2):
    if count % 3 == 0:
        valores += 1
        soma += count

print(f'A soma dos {valores} é igual a {soma}')
