# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quanidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado. 

cores = {
    'roxo':'\033[35m',
    'normal':'\033[m'
}

dias = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos km você percorreu? '))

total = (dias * 60) + km * 0.15

print(f"Esse é o valor total que você irá pagar por esse carro: {cores['roxo']}R${total:.2f}{cores['normal']}")