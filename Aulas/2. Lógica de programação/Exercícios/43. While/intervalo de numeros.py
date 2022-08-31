# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = input('Insira um Número: ')
n2 = input('Insira outro número: ')

if n1.isnumeric() == False or n2.isnumeric() == False:
    print('Por Favor, insira apenas números inteiros!')
else: 
    n1 = int(n1)  
    n2 = int(n2)
    
print(f'Intervalo entre os números {n1} e {n2}')
while n1 < n2: 
    n1 += 1
    if n1 == n2:
        break
    print(n1)

while n1 > n2: 
    n1 -= 1
    if n1 == n2:
        break
    print(n1)
