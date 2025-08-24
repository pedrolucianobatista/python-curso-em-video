# Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços. 

palavra = str(input('Digite uma palavra: ').strip().lower().replace(' ', ''))
word = ''

for count in range(palavra.__len__() - 1, -1, -1):
    word += palavra[count]

print(f'O inverso de {palavra.upper()} é {word.upper()}')

if palavra == word: 
    print(f'A frase {palavra} digitada é um \033[32mpalindromo\033[m!')
else: 
    print(f'A frase {palavra} digitada não é um \033[31mpalindromo\033[m!')

    