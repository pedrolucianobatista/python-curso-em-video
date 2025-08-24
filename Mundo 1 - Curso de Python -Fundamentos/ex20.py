# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import shuffle 

cores = {
    'verde':'\033[32m',
    'normal':'\033[m'
}

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = shuffle(lista)

print(f"Ordem sorteada: {cores['verde']}{lista}{cores['normal']}")
