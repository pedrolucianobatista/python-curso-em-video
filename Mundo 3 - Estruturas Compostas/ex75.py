# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 
# A) Quantas vezes apareceu o valor 9. 
# B) Em que posição foi digitado o primeiro valor 3. 
# C) Quais foram os números pares. 

teste = int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))

valor9 = pares = 0

for count in range(0, 4):
    if teste[count] == 9:
        valor9 += 1
    if teste[count] == 3: 
        valor3 = count

print(f'Você digitou os valores: {teste}')
print(f'O valor 9 apareceu {valor9} vezes')

if 3 in teste: 
    print(f'O valor 3 apareceu na {valor3 + 1}ª posição.')
else: 
    print(f'O valor 3 não foi digitado nenhuma vez.')

print(f'Os valores pares digitados foram ', end='')

for count in range(0, 4): 
    if teste[count] % 2 == 0: 
        print(teste[count], end=' ')
