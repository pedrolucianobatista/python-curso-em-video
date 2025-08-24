# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m', 
    'amarelo':'\033[33m',
    'preto':'\033[36m',
    'normal':'\033[m'
}

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5: 
    print(f"{cores['vermelho']}A sua média foi de {media:.2f}, e você foi REPROVADO!{cores['normal']}")
elif media >= 5 and media <= 6.9:
    print(f"{cores['amarelo']}A sua média foi de {media:.2f}, e você está de RECUPERAÇÃO!{cores['normal']}")
elif media > 10: 
    print(f"{cores['preto']}Reinicie o programa, pois você digitou alguma nota de forma errada.{cores['normal']}")
else: 
    print(f"{cores['verde']}A sua média foi de {media:.2f}, e você foi APROVADO!{cores['normal']}")
