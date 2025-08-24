# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogos. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
 
jogador = {}
gols = []
auxiliar = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partida = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for i in range(0, partida): 
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    auxiliar += gols[i]

jogador['gols'] = gols
jogador['total'] = auxiliar

print('-=' * 30)
print(jogador)
print('-=' * 30)

for indice, valor in jogador.items(): 
    print(f'O campo {indice} tem o valor {valor}.')

print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {partida} partidas')

for i in range(0, partida): 
    print(f'    => Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {jogador['total']} gols.')
