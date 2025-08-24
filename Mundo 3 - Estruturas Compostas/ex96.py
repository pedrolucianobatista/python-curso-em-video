# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(): 
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    print(f'A área de um terreno {largura}x{comprimento} é de {largura * comprimento}m.')

print('Controle de Terrenos'.center(25))
print('-' * 25)

figura = area()
