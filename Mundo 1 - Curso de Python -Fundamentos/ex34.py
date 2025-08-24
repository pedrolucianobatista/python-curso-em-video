# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

cores = {
    'verde':'\033[32m',
    'normal':'\033[m'
}

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250: 
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f"O novo salário do funcionário é de {cores['verde']}R${aumento:.2f}{cores['normal']}")
