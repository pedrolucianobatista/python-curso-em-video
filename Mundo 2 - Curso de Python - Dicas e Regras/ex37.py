# Escreva um programa que leia um númmero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 - para binário
# 2 - para octal 
# 3 - para hexadecimal 

cores = {
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

decimal = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('''[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1: 
    binario = bin(decimal)[2:]
    print(f"DECIMAL: {decimal}  BINÁRIO: {binario}")
elif opcao == 2:
    octal = oct(decimal)[2:]
    print(f"DECIMAL: {decimal}  OCTAL: {octal}")
elif opcao == 3: 
    hexadecimal = hex(decimal)[2:]
    print(f"DECIMAL: {decimal}  OCTAL: {hexadecimal}")
else: 
    print(f"{cores['vermelho']}OPÇÃO INVÁLIDA!{cores['normal']}")