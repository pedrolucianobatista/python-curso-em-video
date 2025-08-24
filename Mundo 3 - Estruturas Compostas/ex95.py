# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 

temp = {}
jogador = []
gols = []
total = 0

while True: 
    print('-' * 30)
    temp['nome'] = str(input('Nome do Jogador: '))
    temp['partidas'] = int(input(f'Quantas partidas {temp['nome']} jogou? '))
    for i in range(0, temp['partidas']): 
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
        total += gols[i]
        temp['gols'] = gols.copy()
    temp['total'] = total
    jogador.append(temp.copy())
    resposta = str(input('Quer continuar? [S/N] '))[0].lower()
    if 'n' in resposta: 
        break

print('-=' * 30)
print(jogador)
print('cod nome         gols        total')
print('-' * 30)

for i in range(0, len(jogador)):
    print(f'  {i} {jogador[i]['nome']} {jogador[i]['gols']} {jogador[i]['total']}') 

while True:
    print('-' * 30)
    valor = int(input('Mostrar dados de qual jogador? '))
    if valor == 999: 
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogador[valor]['nome']}')
    for i in range(0, jogador[valor]['partidas']): 
        print(f'No jogo {i} fez {gols[i]} gols')
        