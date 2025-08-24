# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: 
# escreva('Olá, Mundo!')
# Saída: 
# -----------
# Olá, Mundo!
# -----------

def escreva(texto): 
    size = len(texto);

    print(f'-' * size);
    print(texto);
    print(f'-' * size);

mensagem = input('Digite uma mensagem, e veja a com tamanho adaptável: ');

escreva(mensagem);
