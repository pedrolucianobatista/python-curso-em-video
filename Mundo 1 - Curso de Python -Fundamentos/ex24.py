# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

cidade = input(str('Digite o nome da sua cidade: '))

if cidade.lower().strip().split()[0] == 'santo': 
    print(f"{cores['verde']}True{cores['normal']}")
else: 
    print(f"{cores['vermelho']}False{cores['normal']}")
