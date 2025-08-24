# Elaborar um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# - Â vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros.

cores = {
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

preco = float(input('Qual é o preço do seu produto? R$'))

print('=' * 45)
print('1- À vista dinheiro/cheque: 10% de desconto.')
print('2- À vista no cartão: 5% de desconto.')
print('3- Em até 2x no cartão.')
print('4- 3x ou mais no cartão.')
print('=' * 45)

metodo = int(input('Qual será a opção de pagamento? ').strip())

valor = 0

if 1 == metodo: 
    valor = preco * 0.9
    print(f"Esse é o valor a ser pago R${valor:.2f}")
elif 2 == metodo: 
    valor = preco * 0.95
    print(f"Esse é o valor a ser pago R${valor:.2f}")
elif 3 == metodo: 
    valor = preco / 2
    print(f"O pagamento será realizado em duas parcelas de R${valor:.2f}")
elif 4 == metodo: 
    parcelas = int(input('Quantas parcelas? '))
    valor = preco * 1.2 / parcelas
    print(f"O total do pagamento será de R${preco * 1.2:.2f}, e cada uma custará R${valor:.2f}")
else: 
    print(f"{cores['vermelho']}OPÇÃO INVÁLIDA!{cores['normal']}")