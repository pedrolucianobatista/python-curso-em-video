# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha. 

lista = [[], [], []]
somaP = somaT = maior = 0

for i in range(0, 3): 
    for j in range(0, 3): 
        lista[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if lista[i][j] % 2 == 0: 
            somaP += lista[i][j]
        if j == 2: 
            somaT += lista[i][j]
        if i == 1: 
            if lista[i][j] > maior: 
                maior = lista[i][j]

print('-=' * 30)

for i in range(0, 3): 
    for j in range(0, 3): 
        print(f'[ {lista[i][j]:^5} ]', end = '')
    print()
    
print('-=' * 30)
print(f'A soma dos valores pares é {somaP}.')
print(f'A soma dos valores da terceira coluna é {somaT}.')
print(f'O maior valor da segunda linha é {maior}.')