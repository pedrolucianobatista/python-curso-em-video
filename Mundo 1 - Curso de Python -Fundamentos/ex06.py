# Crie um algoritmo que leia um número e mostre o seu dobro, tiplo e raiz quadrada. 

valor = int(input('\033[35mDigite um número: '))

print("O dobro de {} é igual a {}".format(valor, valor * 2))
print("O triplo de {} é igual a {}".format(valor, valor * 3))
print("A raiz quadrada de {} é igual a {:.2f}".format(valor, valor ** (1 / 2)))
