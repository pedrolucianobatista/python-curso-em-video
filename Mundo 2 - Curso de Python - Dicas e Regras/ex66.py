# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). 

contador = soma = 0

print('Obs: Para cancelar é só digitar o número 999!')

while True: 
    valor = int(input('Digite um número: '))
    if valor == 999: 
        break
    contador += 1 
    soma += valor

print(f'Você digitou {contador} números!')
print(f'A soma é de {soma}!')
