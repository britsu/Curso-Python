# Exemplo de estrutura de repetição
x = 1

while x < 10:
    print(x)
    x = x + 1
print("Valor de x após a finalização do loop: ", x)

# Instrução break: Para o loop mesmo se a condição while for verdadeira
l = 1
while l < 10:
    if l == 5:
        print(l)
        print('l é igual a: ', l)
        break
    print(l)
    l = l + 1
# Instrução continue: faz com que o interpretador salte para o proximo laço
c = 5
while c < 20:
    if c == 13:
        c = c + 1
        continue
    print(c)
    c = c + 1

print("uau")
print("este é o valor de c: ", c)

# Calculadora basica:
n1 = float(input('Digite um número: '))
op = input('Digite a operação: ')
n2 = float(input('Digite outro número: '))
op = op.replace(" ", "")  # Removendo possíveis espaços em branco

if op == '+':
    print('Resultado: ', n1 + n2)
elif op == '-':
    print('Resultado: ', n1 - n2)
elif op == '*':
    print('Resultado: ', n1 * n2)    
elif op == '/':
    print('Resultado: ', n1 / n2)
else:
    print("Erro na operação!")