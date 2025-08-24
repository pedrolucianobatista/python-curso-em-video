# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

answer = 'no'
counter = 0
values = [] 

while True: 
    values.append(int(input('Enter a number: ')))
    if values.count(values[counter]) == 1: 
        print('New element...')
        counter += 1
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = str(input('Do you want to continue? [Y/N] '))[0].strip().lower()
            if answer == 'n': 
                break;
            elif answer != 'y': 
                print('Wrong answer! Enter with the answer again.')
    else: 
        del values[counter]
        print("Repeated element! I'm not add...")
        answer = ''
        while answer != 'n' and answer != 'y':
            answer = str(input('Do you want to continue? [Y/N] '))[0].strip().lower()
            if answer == 'n': 
                break;
    if answer == 'n': 
        break;

print('-=-' * 10)

values.sort()

print(values)
