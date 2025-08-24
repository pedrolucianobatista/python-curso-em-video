# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: 
# n = leiaint('Digite um n')

def leiaInt(x): 
    x = input(x)
    while True:
        if x.isnumeric():
            return x
            break
        else: 
            print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
            x = input('Digite um número: ')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
