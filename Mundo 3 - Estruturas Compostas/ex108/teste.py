# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostra os valores como um valor monetário formatado

from moeda import metade, dobro, aumentar, moeda

p = float(input('Digite o preço: '))

print(f'A metade de R${moeda(p)} é R${moeda(metade(p))}')
print(f'O dobro de R${moeda(p)} é R${moeda(dobro(p))}')
print(f'Aumentando 10%, temos R${moeda(aumentar(p, 10))}')
