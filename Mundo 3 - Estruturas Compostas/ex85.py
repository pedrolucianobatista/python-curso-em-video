# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. 

lista = []
par = []
impar = []

for i in range(0, 7): 
    lista.append(int(input(f'Digite o {i + 1}º valor: ')))
    if lista[i] % 2 == 0: 
        par.append(lista[i])
    else: 
        impar.append(lista[i])

print('-=' * 20)

par.sort()
impar.sort()

print(f'Esses foram os valores pares digitados: {par}')
print(f'Esses foram os valores ímpares digitados: {impar}')
