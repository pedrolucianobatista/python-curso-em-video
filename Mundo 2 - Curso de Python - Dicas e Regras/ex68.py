# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

computer = randint(0, 10)

print(15 * '-=')    
print('VAMOS JOGAR PAR OU ÍMPAR')
print(15 * '-=')

win = 0

while True: 
    soma = 0
    answer = ''
    resultado = ''
    human = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ').lower().strip())
    print(30 * '-')
    soma = human + computer
    if opcao == 'i':
        answer = 'ÍMPAR'
    else: 
        answer = 'PAR'
    if soma % 2 == 0: 
        resultado = 'PAR'
        print(f'Você jogou {human} e o computador {computer}. Total de {soma} DEU {resultado}')
    else: 
        resultado = 'IMPAR'
        print(f'Você jogou {human} e o computador {computer}. Total de {soma} DEU ÍMPAR.')
    print(30 * '-')
    if resultado[0].lower() == opcao:
        win += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(15 * '=-')
    elif resultado[0].lower() != 'p' and resultado[0].lower() != 'i':
        print('OPÇÃO INVÁLIDA!') 
    else: 
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {win} vezes.')
        print(15 * '=-')
        break
