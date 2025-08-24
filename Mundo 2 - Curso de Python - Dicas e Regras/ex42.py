# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# Equilátero: Todos os lados iguais 
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('DIgite o terceiro lado do triângulo: '))

if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado2 < lado1 + lado3:
    print('Isso é TRIÂNGULO!')
    if lado1 == lado2 == lado3:
        print('TRIÂNGULO EQUILÁTERO!')
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('TRIÂNGULO ESCALENO!')
    else: 
        print('TRIÂNGULO ISÓSCELES!')
else: 
    print('Isso não é um TRIÂNGULO!')
