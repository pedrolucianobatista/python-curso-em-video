# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. 
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. 

from utilidadeCev.listar.index import listarPessoas
from utilidadeCev.cadastrar.index import cadastrarPessoas
from utilidadeCev.tratar.index import tratarErros

def menuPrincipal(): 
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print('\033[33m1\033[0m - \033[34mVer pessoas cadastradas\033[0m')
    print('\033[33m2\033[0m - \033[34mCadastrar nova Pessoa\033[0m')
    print('\033[33m3\033[0m - \033[34mSair do Sistema\033[0m')
    print('-' * 40)

while True:
    menuPrincipal()
    valor = tratarErros()

    if (valor == 1): 
        listarPessoas()
    elif (valor == 2): 
        cadastrarPessoas()
    else: 
        break
