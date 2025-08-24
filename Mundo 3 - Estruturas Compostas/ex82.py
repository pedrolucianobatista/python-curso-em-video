# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. 

counter = 0
pair = []
list = []
odd = []

while True: 
    list.append(int(input('Enter a number: ')))
    if list[counter] % 2 == 0: 
        pair.insert(counter, list[counter])
    else:
        odd.insert(counter, list[counter])
    answer = (str(input('Do you want to continue? [y/n] ')))[0].lower()
    counter += 1
    if 'n' in answer: 
        break;
    elif answer != 'n' and answer != 'y': 
        while True: 
            print('Invalid answer! Try again.') 
            answer = (str(input('Do you want to continue? [y/n] ')))[0].lower()
            if answer == 'n' or answer == 'y': 
                break;

print('-=' * 15)
print(f'The full list is {list}')
print(f'The list of pairs is {pair}')
print(f'The odds list is {odd}')
