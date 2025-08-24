# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
# Considere US$1.00 = R$5.73    EUR€1.00 = 6.25

real = float(input('Quantos reais você tem? R$'))

dolar = real / 5.73
euro = real / 6.25 

print("Você tem {:.2f}US$".format(dolar))
print("Você tem {:.2f}EUR".format(euro))
