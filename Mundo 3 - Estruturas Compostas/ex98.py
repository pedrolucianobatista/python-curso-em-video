# Faça um programa que tenha uma função chamada contador(), que receba três parãmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) De 1 até 10, de 1 em 1 
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.    # O usuário irá indicar o início, fim e os passos 

  
from time import sleep

print('-=' * 30);
print('Contagem de 1 até 10 de 1 em 1');

for i in range(1, 11):
    print(i, end=' ', flush = True); 
    sleep(0.25);

print('FIM');
print('-=' * 30);
print('Contagem de 10 até 0 de 2 em 2');

for i in range(10, -1, -2): 
    print(i, end = ' ', flush = True); 
    sleep(0.25)

print('FIM');
print('-=' * 30);
print('Agora é sua vez de personalizar a contagem!');

inicio = int(input('Início: ')); 
fim = int(input('Fim: ')); 
passo = int(input('Passo: ')); 

if (fim > inicio): 
    for i in range(inicio, fim + 1, passo): 
        print(i, end = ' ', flush = True); 
        sleep(0.25);
else: 
    for i in range(inicio, fim - 1, passo): 
        print(i, end = ' ', flush = True);
        sleep(0.25);

print();
print('-=' * 30);
