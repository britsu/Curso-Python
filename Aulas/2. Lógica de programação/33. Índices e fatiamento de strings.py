# Índices positivos:
# Índice: [0123456789] 
texto  =  'Luis lindo'

# Podemos trabalhar apenas com um caractere especificando o índice logo após a variável:
print(texto[1])

# Também podemos trabalhar com partes da string, da seguinte forma;
# Do 2° caractere até o final:
print(texto[1:])
# Do inicio até o 7° caractere:
print(texto[:8]) # Podemos perceber que o caractere final não é considerado, por isso utilizamos o 8
# Do 3o caractere até o 7°
print(texto[3:8])

# Índices negativos

texto  =      'Luis gato'
# negativos: -[987654321] (O sinal - deve ser incluso antes de todos os índices negativos)

# Exibindo apenas um caractere (negativo):
print(texto[-3])
# Exibindo todo o texto sem o último caractere:
print(texto[:0])
