# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

cores = {
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'roxo':'\033[35m',
    'azul':'\033[36m',
    'normal':'\033[m'
}

altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))

imc = peso / (altura ** 2)

print(f"O seu IMC está em {imc:.2f}")

if imc < 18.5: 
    print(f"{cores['amarelo']}Abaixo do peso!{cores['normal']}")
elif 18.5 <= imc < 25:
    print(f"{cores['verde']}Peso ideal!{cores['normal']}") 
elif 25 <= imc < 30:
    print(f"{cores['azul']}Sobrepeso!{cores['normal']}")
elif 30 <= imc < 40:
    print(f"{cores['vermelho']}Obesidade!{cores['normal']}")
else: 
    print(f"{cores['roxo']}Obesidade mórbida!{cores['normal']}")
