from utilidadeCev.tratar.index import tratamentoInt

pessoa = []

def cadastrarPessoas(): 
    print('-' * 40)
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    nome = str(input('Nome: '))
    idade = tratamentoInt() 

    pessoa.append({"nome": nome, "idade": idade})

def mostrarCadastros(): 
    for i in range(len(pessoa)):
        print(f'{pessoa[i]["nome"]:<25} {pessoa[i]["idade"]} anos')
