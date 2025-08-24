# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. 

from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

tuple = (n1, n2, n3, n4, n5)
maior = 0 
menor = 0

for count in range(0, 5): 
    if tuple[count] > maior: 
        maior = tuple[count]
    if count == 0:
        menor = tuple[count]
    if menor > tuple[count]: 
        menor = tuple[count]

print(f'Os valores sorteados foram: {tuple}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
