# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

valor = float(input('Qual é o valor da residência? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input(f"Em quanto tempo o você pretende quitar o valor de R${valor:.0f}? "))

parcela = valor / (anos * 12)

if salario * 0.3 < parcela: 
    print(f"{cores['vermelho']}EMPRÉSTIMO NEGADO!{cores['normal']}\nPois a parcela é de R${parcela:.2f}, e execede 30% do seu salário que é R${salario * 0.3:.2f}")
else: 
    print(f"{cores['verde']}EMPRÉSTIMO ACEITO!{cores['normal']}\nE a sua parcela será de R${parcela:.2f} por mês durante {anos:.2f} anos")
