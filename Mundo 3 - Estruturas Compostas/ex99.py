# Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior. 

from time import sleep 

def maior(*args):
    length = len(args); 

    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(1.5)

    print(*args, end=' ')

    print(f'Foram informados {length} valores ao todo.')

    if length == 0:
        print('O maior valor informado foi 0.')
    else: 
        for i in range(0, length): 
            if (i == 0): 
                maior = args[0]; 
            elif (args[i] > maior): 
                maior = args[i]
        print(f'O maior valor digitado foi o {maior}'); 

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
