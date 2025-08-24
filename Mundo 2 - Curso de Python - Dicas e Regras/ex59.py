# Crie um programa que leia dois valores e mostre um menu na tela: 
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números 
# [ 5 ] Sair do programa 
# Seu programa deverá realizar a operação solicitada em cada caso. 

from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
answer = 0
maior = 0

while answer != 5: 
    print('   [1] somar')
    print('   [2] multiplicar')
    print('   [3] maior')
    print('   [4] novos números')
    print('   [5] sair do programa')
    answer = int(input('Digite a opção desejada: ')) 
    if answer == 1: 
        print(f'A soma entre {valor1} e {valor2} é de {valor1 + valor2}')
    elif answer == 2: 
        print(f'O produto entre {valor1} e {valor2} é igual a {valor1 * valor2}')
    elif answer == 3: 
        if valor1 > valor2: 
            maior = valor1
            print(f'Entre o valor {valor1} e o {valor2}, o maior é o {maior}')
        elif valor2 > valor1: 
            maior = valor2
            print(f'Entre o valor {valor1} e o {valor2}, o maior é o {maior}')
        else: 
            print('Os valores são iguais!')
    elif answer == 4: 
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif answer == 5: 
        print('Finalizando...')
        sleep(1)
        print('Obrigado por ter participado')
    else: 
        print('Opção inválida. Tente novamente.')
    print(9 * '-=-')