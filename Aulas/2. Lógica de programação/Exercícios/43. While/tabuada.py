# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

num = input('Insira um número entre 0 e 10: ')

if num.isnumeric() == True:
    num = int(num)
    if num >= 0 and num <= 10:
        print(f'TABUADA DO {num}:\n')
        mult = 0
        while mult <= 10:
            resultado = num * mult
            print(f'{num} X {mult} = {resultado}')
            mult += 1
        
    else:
        print('Insira um número entre 0 e 10')    
else:
    print('Por favor, digite um valor numérico')