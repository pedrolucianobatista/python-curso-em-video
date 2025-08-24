# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista 

list = []
aux = 0

while True: 
    list.append(int(input('Enter a number: ')))
    answer = str(input('Do you want to continue? [Y/N] ')).lower().strip()[0]
    if 'n' in answer: 
        break;
    while answer != 'n' and answer != 'y': 
        print('Invalid option! Try again.')
        answer = str(input('Do you want to continue? [Y/N] ')).lower().strip()[0]

for count in range(0, len(list)): 
    for counter in range(count + 1, len(list)): 
        if list[count] < list[counter]: 
            aux = list[count]
            list[count] = list[counter]
            list[counter] = aux
            
print(f'You entered {len(list)} elements')
print(f'The elements in order decrescent are {list}')
print("The value 5 it's in list" if 5 in list else "The value it's not in list")
