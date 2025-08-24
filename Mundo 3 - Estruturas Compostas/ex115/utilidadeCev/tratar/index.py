def tratarErros(): 
    while True: 
        try: 
            valor = int(input('\033[33mSua Opção: \033[0m'))

            if (valor > 3 or valor <= 0): 
                print('\033[31mValor inválido! O intervalo das opções vai de 1 a 3\033[0m')
            else: 
                return valor
        except: 
            print('\033[31mValor inválido!\033[0m')

def tratamentoInt(): 
    while True: 
        try: 
            idade = int(input('Idade: '))
            return idade 
        except: 
            print('\033[31mValor inválido!\033[0m')
