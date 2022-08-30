"""
Operadores:
and  (E)
or   (OU)
not  (NÃO)
in   (Inserido | Existe em)
"""
# Verificando se há algum caractere em uma frase:
frase = input('Informe alguma frase: ')
caractere = input('Caractere a ser verificado: ')
if caractere == frase:
    print(f'O caractere "{caractere}" é igual a frase: {frase}')
elif caractere in frase:
    print(f'O caractere "{caractere}" existe na frase: {frase}')
elif caractere not in frase:
    print(f'O caractere "{caractere}" não existe na frase: {frase}')
else:
    print('Por favor, insira somente dados válidos!')

    