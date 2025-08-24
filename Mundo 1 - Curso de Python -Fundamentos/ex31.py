# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longes. 

cores = {
    'azul':'\033[36m',
    'amarelo':'\033[33m',
    'normal':'\033[m'
}

distancia = float(input('Digite a distância total da sua viagem em Km: '))

if distancia >= 200:
    resultado = distancia * 0.45
else:
    resultado = distancia * 0.5
print(f"Para uma viagem de {cores['azul']}{distancia}km{cores['normal']}, nós vamos desembolsar {cores['amarelo']}R${resultado}{cores['normal']}")

print(f"Esse é o valor da sua viagem {cores['azul']}R${distancia * 0.45:.2f}{cores['normal']}' if distancia >= 200 else f'Esse é o valor da sua viagem {cores['amarelo']}R${distancia * 0.5:.2f}{cores['normal']}")
