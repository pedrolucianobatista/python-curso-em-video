# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso. 

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 
    valor = int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20: 
        print(f'Você digitou o número {cont[valor]}')
        break
    print('Tente novamente. ', end='')

while True: 
    resposta = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    if resposta in 's':
        while True: 
            valor = int(input('Digite um número entre 0 e 20: '))
            if 0 <= valor <= 20: 
                print(f'Você digitou o número {cont[valor]}')
                break
            print(f'Tente novamente. ', end='')
    if resposta == 'n': 
        break
    print('Tente novamente. ', end='')
