# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite. 

from time import sleep

cores = {
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

print(f"{cores['amarelo']}{'-=-'*10}{cores['normal']}")
print(f"{cores['amarelo']}RADAR...{cores['normal']}")
print(f"{cores['amarelo']}{'-=-'*10}{cores['normal']}")

velocidade = float(input(f"{cores['amarelo']}Digite a velocidade que se encontra o seu veículo: {cores['normal']}"))

print(f"{cores['amarelo']}CALCULANDO...{cores['normal']}")
sleep(1)

excedente = (velocidade - 80) * 7

if velocidade > 80:
    print(f"{cores['vermelho']}A sua multa é de R${excedente:.2f}. Observação: É R$7,00 cada km excedido{cores['normal']}")
else: 
    print(f"{cores['verde']}Velocidade permitida!{cores['normal']}")
