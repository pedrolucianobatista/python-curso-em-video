# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for counter in range(len(tupla)): 
    print(f'Na palavra {tupla[counter]} temos', end='')

    for count in range(len(tupla[counter])): 
        if tupla[counter][count] in 'AEIOU': 
            print(end=' ' f'{tupla[counter][count].lower()}')

    print('')
