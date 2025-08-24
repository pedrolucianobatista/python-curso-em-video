# Faça um mini-sistema que utilize o Interactive Help do Python. O usuáio vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. 

def interactiveHelp(valor): 
    texto1 = 'SISTEMA DE AJUDA PYHELP'
    while True: 
        print(f"\033[42m\033[97m {(len(texto1) + 2) * '~'}")
        print({texto1.center(len(texto1) + 2)})
        print(f"{(len(texto1) + 2) * '~'}\033[0m")
        x = input(valor).lower() 
        frase = (f"Acessando o manual do comando '{x}'")
        print(f"\033[44m\033[97m{(len(frase) + 2) * '~'}")
        print(f'{frase.center(len(frase) + 2)}')
        print(f"{(len(frase) + 2) * '~'}\033[0m")
        if x != 'fim':
            return help(x) 
        else: 
            return

teste = interactiveHelp('Função ou Biblioteca > ')
print(f"\033[47m\033[30m{teste}\033[0m")
