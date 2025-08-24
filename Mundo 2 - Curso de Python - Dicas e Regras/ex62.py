# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostarr mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 

print('Gerador de PA')
print('-=' * 10)

first = int(input('Digite o primeiro termo da PA: '))
reason = int(input('Digite o valor da razão da PA: '))

second = first
counter = 0
new_counter = 0

while counter < 10: 
    print(second + counter * reason,'➔ ', end = ' ')
    counter += 1

print('PAUSA')

answer = 1

while answer > 0: 
    answer = int(input('Quantos termos você quer mostrar a mais? '))
    if answer > 0: 
        new_counter = answer + counter
        while counter < new_counter: 
            print(second + counter * reason, '➔ ', end = ' ')
            counter += 1 
        print('PAUSA')

print(f'Progressão finalizada com {new_counter} termos mostrados.')
