# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True: 
    contador = 1
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print(35 * '-')
    if valor < 0: 
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break; 
    while contador <= 10: 
        print(f'{valor} x {contador:2} = {valor * contador}')
        contador += 1
    print(35 * '-')
