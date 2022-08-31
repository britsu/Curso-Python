# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = input('Insira uma nota entre 0 e 10: ')
    if nota.isnumeric() == True:    
        nota = float(nota)
        if nota >= 0 and nota <=10:
            print(f'A nota {nota} é válida!')
            break
        else:
            print(f'A nota {nota} não está entre 0 e 10!, por favor, insira uma nota entre 0 e 10')
    elif nota.isnumeric() == False:
        print('O valor inserido não é um valor numérico')

