# Exemplo de uso da função len()
nome = 'Luis Henrick.'
print(len(nome))  # 13

# Exercício - usuário 10 caracteres
usuario = input('Insira seu nome de usuário: ')
senha = input('Insira sua senha: ')

if (len(usuario) > 0 and len(usuario) <= 10 and len(senha) > 0 and len(senha) <=20):
    print('Usuário e senha validos!')
else:
    print('Usuário ou senha inválidos')