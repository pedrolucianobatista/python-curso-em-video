# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando uma laço for.

valor = int(input('Digite o valor para ver a tabuada: '))

for count in range(1, 11):
    print(f'{count:2} x {valor} = {count * valor}')
