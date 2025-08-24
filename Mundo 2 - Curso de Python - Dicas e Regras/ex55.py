 # Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. 

for count in range(1, 6): 
    kilos = float(input(f'Digite quantos Kg tem a {count}º pessoa: '))
    if count == 1: 
        menor = kilos
        maior = kilos
    if kilos > maior: 
        maior = kilos
    if kilos < menor: 
        menor = kilos

print(f'Mais pesado {maior:.2f}Kg')
print(f'Menos pesado {menor:.2f}Kg')
