# Faça um programa que leia uma frase pelo teclado e mostre: 
# * Quantas vezes aparece a letra "A"
# * Em que posição ela aparece a primeira vez.
# * Em que posição ela aparece a última vez. 

cores = {
    'roxo':'\033[35m',
    'normal':'\033[m'
}

frase = str(input('Digite uma frase: ').lower().strip())

print(f"Quantas vezes aparece a letra 'A': {cores['roxo']}{frase.count('a')}{cores['normal']}\nEm que posição ela aparece a primeira vez: {cores['roxo']}{frase.find('a') + 1}{cores['normal']}\nEm que posição ela aparece a última vez: {cores['roxo']}{frase.rfind('a') + 1}{cores['normal']}")
