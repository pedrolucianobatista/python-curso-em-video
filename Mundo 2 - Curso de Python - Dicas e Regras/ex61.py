# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. 

first = int(input('Digite o primeiro valor da PA: '))
reason = int(input('Digite o valor da razão da PA: '))

counter = 0 

while counter < 10: 
    print(first + reason * counter, ' ➔ ', end = ' ')
    counter += 1

print('FIM')
