# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# * A média de idade do grupo. 
# * Qual é o nome do homem mais velho. 
# * Quantas mulheres têm menos de 20 anos. 

media = 0
soma = 0
old = ''
maior = 0
mulheres = 0

for count in range(1, 5):
    nome = str(input(f'Digite o nome da {count}º pessoa: '))
    sexo = str(input(f'Qual é o sexo do(a) {nome}: ').strip().lower())
    idade = int(input(f'Qual é a idade do(a) {nome}: '))
    soma += idade
    if sexo == 'masculino' and idade > maior: 
        maior = idade
        old = nome
    if sexo == 'feminino' and idade < 20:
        mulheres += 1

media = soma / 4

print(f'A média de idade das pessoas é de {media:.2f}')
print(f'O homem mais velho é o {old} com a idade de {maior} anos')
print(f'Neste grupo temos {mulheres} mulheres com menos de 20 anos')
