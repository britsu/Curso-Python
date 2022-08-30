'''
Quais são os modificadores?
:s - Textos (Strings)
:d - Inteiros (Digit)
:f - Números não inteiros (Float)
'''
# Exemplos de uso:

# Casas decimais
numero_float = 9.12345678
print('Saída 2: {0:.2f}'.format(numero_float))

# Porcentagem
valor = 5.5 / 40.0

print(
  f'Resultado original: {valor}\n'
  f'Resultado formatado: {valor:.1%}'
)

# formatação de preenchimento
valor1 = 255
print(f"{valor1:->10}")
