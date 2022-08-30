"""
Operadores:
==   Igual
!=   Diferente
>    Maior que
<    Menor que
>=   Maior ou igual a
<=   Menor ou igual a 
"""
# Exercício - Empréstimo
# Uma pessoa só pode solicitar um empréstimo se for maior de idade
nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))

if idade >= 18:
    print(f'Empréstimo Autorizado, {nome}')
else:
    print(f'Empréstimo Negado, {nome}') 
    