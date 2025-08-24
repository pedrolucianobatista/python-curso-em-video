# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 

expression = str(input('Enter an expression: '))
left = expression.count('(')
right = expression.count(')')

if left != right or '()' in expression: 
    print('Invalid expression!')
else: 
    print('Valid expression')
