def aumentar(preco=0, taxa=0, formato=False): 
    '''
    -> Calcula o aumento de um determinado preço, 
    retornando o resultado com ou sem formatação. 
    :param preço: o preço que se quer reajustar 
    :param taxa: qual é a porcentagem do aumento. 
    :param formato: quer a saída formatada ou não 
    :return: o valor reajustado, com ou sem formato. 
    '''
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False): 
    res = preco * 2 
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False): 
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'): 
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(valor=0, aumento=10, desconto=5): 
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f'{"Preço analisado:":<20} {moeda(valor)}')
    print(f'{"Dobro do preço:":<20} {dobro(valor, True)}')
    print(f'{"Metade do preço:":<20} {metade(valor, True)}')
    print(f'{aumento}% de aumento:'.ljust(20), aumentar(valor, aumento, True))
    print(f'{desconto}% de redução:'.ljust(20), diminuir(valor, desconto, True))
    print('-' * 30)
