# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. 

def fatorial(a, show = False): 
    """
    fatorial(n, show=False)
    -> Calcula o Fatorial de um número. 
    :param n: O número a ser calculado. 
    :param show: (opcional) Mostrar ou não a conta. 
    :return: O valor do Fatorial de um número n.
    """
    contador = 1 
    if show == False: 
        for i in range(a, 0, -1):
            contador = i * contador
        return contador
    else: 
        for i in range(a, 0, -1): 
            contador = i * contador
            if i > 1: 
                print(f'{i} x', end = ' ')
            else: 
                print(end = ''f'{i} = ')
        return contador
print('-' * 30)
print(fatorial(5, False))
