# Faça um programa que leia a largura e a altura de uma parede em metro, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados. 

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
litro = area / 2

print("Essa é a área do seu espaço: {:.2f}m".format(area))
print("Essa é a quantidade de litros de tinta necessária para pintar a parede: {:.2f}l".format(litro))
