# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. 
# def ficha(nome = '', gols = 0): 
# Retornar com a string mostrando as informações
# Realizar uma verificação antes de "chamar" a função
# Acredito que não tenha problemas uma variável sem valor, mas sim a questão da função
# Strings podem ficar vazias, fazer vericação apenas para a questão dos gols. 
# Começar a string com um valor, e depois altera-la ao longo do código

def calcular(jogador = '', gols = 0): 
    if jogador.strip() == '': 
        jogador = '<desconhecido>'
    if gols.strip() == '':  
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) ao total.')

nome = str(input('Nome de Jogador: '))
goals = str(input('Número de Gols: '))

calcular(nome, goals)
