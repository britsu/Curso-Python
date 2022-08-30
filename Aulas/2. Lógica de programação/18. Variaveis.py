# Logo após a atribuição de valores, estão comentados os tipos de variáveis para facilitar o entendimento.
nome = 'luis'  # str
sobrenome = 'brito'  # str
idade = 17  # int
altura = 1.80  # float
peso = 70
maioridade = idade > 18  # boolean

# Usando os dados
print('Nome completo: ', nome,  sobrenome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade?', maioridade)

# Desafio: Calcular o IMC do britin
imc = peso // (altura ** 2)
print('IMC do', nome, sobrenome, 'é: ', imc, 'e ele tem ', idade, 'anos de idade.')
