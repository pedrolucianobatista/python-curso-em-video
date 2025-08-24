# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando flag).

value = sum = counter = 0

while value != 999: 
    value = int(input('Digite um número [999 para parar]: '))
    if value != 999: 
        sum += value
        counter += 1

print(f'Você digitou {counter} números e a soma entre eles foi de {sum}.')
