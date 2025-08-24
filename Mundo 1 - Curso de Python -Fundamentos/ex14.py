# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

cores = {
    'vermelho':'\033[31m',
    'normal':'\033[m'
}

celsius = float(input('Digite a temperatura em celsius: '))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperatura em Fahrenheit: {cores['vermelho']}{fahrenheit:.2f}°f{cores['normal']}")
