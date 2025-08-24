# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome dos alunos e escrevendo o nome do escolhido. 

from random import choice

cores = {
    'verde':'\033[32m',
    'normal':'\033[m'
}

aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

print(f"Esse foi o aluno(a) sorteado: {cores['verde']}{choice(lista)}")
