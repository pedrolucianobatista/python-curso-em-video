# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
# - Quantidade de notas
# - A maior nota 
# - A menor nota 
# - A média da turma 
# - A situação (opcional)
 
def notas(* dados, sit = False): 
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    maior = menor = soma = 0
    situacao = ''
    for i in range(0, len(dados)): 
        soma += dados[i]
        if i == 0: 
            menor = dados[i]
        if dados[i] < menor: 
            menor = dados[i]
        if dados[i] > maior: 
            maior = dados[i]
    dicio['total'] = len(dados)
    dicio['maior'] = maior
    dicio['menor'] = menor
    dicio['media'] = soma / dicio['total']
    if sit: 
        if dicio['media'] >= 6: 
            situacao = 'BOA'
        elif 5 <= dicio['media'] < 6:
            situacao = 'REGULAR'
        else: 
            situacao = 'RUIM'
        dicio['situacao'] = situacao
    return dicio
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit = True)
print(resp)
