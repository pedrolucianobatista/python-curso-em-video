# Crie um programa que escreva "Olá, mundo!" na tela. 

cor = {
    'verde':'\033[32m',
    'branco':'\033[97m',
    'normal': '\033[m'
}

print("{}Olá, mundo!{}".format(cor['verde'], cor['normal']))
