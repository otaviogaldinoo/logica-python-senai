# 4. Suponha que o professor Atila possua dois logins na rede do SENAI-SP. 
# Construa um programa que valide o acesso do professor à rede. 
# Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”.
# Caso contrário, “Usuário e senha não conferem”.
# Dados dos dois logins:
# login 1			login 2
# usuário: atila		usuário: olivi
# senha: 12345		senha: 54321
# Salvar o código como: dois_logins.py

usuario_login1 = 'atila'
senha_login1 = '12345'

usuario_login2 = 'olivi'
senha_login2 = '54321'

usuario_digitado = input('digite o usuario: ')
senha_digitada = input('digite a senha: ')

usuario_logado = False

if usuario_digitado == usuario_login1 and senha_digitada == senha_login1:
    usuario_logado = True
    print(f'seja bem vindo {usuario_login1}')
elif usuario_digitado == usuario_login2 and senha_digitada == senha_login2:
    usuario_logado = True
    print(f'seja bem vindo {usuario_login2}')
else:
    print('usuário e senha não conferem')