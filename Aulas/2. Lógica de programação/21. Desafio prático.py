"""
* Criar variáveis para nome(str),idade(int), altura(float) e peso(float) de uma pessoa
* Criar variável com o ano atual(int)
* Obter o ano de nascimento da pessoa(baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais(peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings(com as chaves)
"""
# Resolução: 
nome = 'Luis'
idade = 17
altura = 1.80
peso = 70
anoAtual = 2022

# Obtendo o ano de nascimento do cara
nasc = anoAtual - idade
print(f'O ano de nascimento de {nome} é {nasc}!')

# Obtendo o IMC do cara (peso/altura²)
imc = peso / altura ** 2
print(f'O IMC de {nome} é {imc:.2f}')

# Resultado final: 
print('Logo, {} nasceu em {},  e após {} anos, tem {} kg, uma altura de {} m, \no que resulta em um IMC de: {:.2f}'.format(nome, nasc, idade, peso, altura, imc))
