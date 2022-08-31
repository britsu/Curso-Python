# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    user = str(input('Insira seu nome de usuário: '))
    senha = str(input('Insira sua senha: '))

    if user == senha:
        print('\nA senha não pode ser igual ao usuário!')
        print('Por favor, tente novamente!\n')
    else:
        print('Login Efetuado!')    
        break
    