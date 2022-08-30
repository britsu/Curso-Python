"""
1.
- Faça um programa que peça ao usuário para digitar um número inteiro
- informe se este número é par ou ímpar. 
- Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
numero = float(input('Informe um número INTEIRO: '))

if (numero % 2) == 0:
    print(f'O número digitado ({numero}) é um número par')
elif (numero % 2) != 0:
    print(f'O número digitado ({numero}) é um número impar')
else:
    print('O valor inserido não é um número inteiro')
    
"""
2. 
- Perguntar Hora ao usuário
- Retornar saudação apropriada
    - Bom dia: 0-11
    - Boa tarde: 12-17
    - Boa noite: 18-23
"""
from itertools import count


hora = int(input('Informe a hora: '))

if hora >=0 and hora <= 11:
    print('Bom dia! ')
elif hora >= 12 and hora <=17:
    print('Boa tarde! ') 
elif hora >=18 and hora <=23:
    print('Boa noite! ')
else:
    print('Informe somente a hora, por favor')
    
"""
3. 
- Solicitar nome do usuário
- 4 letras ou menos: Muito curto
- Entre 5 e 6 letras: Normal
- Maior que 6 letras: Muito grande
"""
nome = input('Insira seu nome: ')

if len(nome) <= 4:
    print('Seu nome é muito curto! ')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal! ')
else:
    print('Seu nome é muito grande! ')
