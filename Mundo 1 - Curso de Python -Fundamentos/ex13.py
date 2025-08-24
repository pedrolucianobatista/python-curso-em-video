# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

cores = {
    'azul':'\033[34m',
    'normal':'\033[m'
}

salario = float(input('Digite o salário do funcionário: R$'))

novoSalario = salario * 1.15

print(f"O novo salário do funcionário é de {cores['azul']}R${novoSalario:.2f}{cores['normal']}")
